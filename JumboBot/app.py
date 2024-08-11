import base64
import sqlite3
import datetime
import sqlite3
import pandas as pd
import asyncio
import aiohttp
import tweepy
from collections import defaultdict
from abc import ABC, abstractmethod
from constant import *
from helpers import *


# Adapters for sqlite
def adapt_date_iso(val):
    return val.isoformat()
def adapt_datetime_iso(val):
    return val.isoformat()
def adapt_datetime_epoch(val):
    return int(val.timestamp())
def convert_date(val):
    return datetime.date.fromisoformat(val.decode())
def convert_datetime(val):
    return datetime.datetime.fromisoformat(val.decode())

def convert_timestamp(val):
    return datetime.datetime.fromtimestamp(int(val))
sqlite3.register_converter("date", convert_date)
sqlite3.register_converter("datetime", convert_datetime)
sqlite3.register_converter("timestamp", convert_timestamp)
sqlite3.register_adapter(datetime.date, adapt_date_iso)
sqlite3.register_adapter(datetime.datetime, adapt_datetime_iso)
sqlite3.register_adapter(datetime.datetime, adapt_datetime_epoch)



class JSONGenerator(ABC):
    @abstractmethod
    def generate_key(self, categories, page) -> str:
        pass

class URLCreator(ABC):
    def __init__(self, json_generator: JSONGenerator) -> None:
        """
        Initialize JSON generator.
        
        Args:
            json_generator (JSONGenerator): instance of the JSONGenerator class.
        """
        self.json_generator = json_generator

    @abstractmethod
    def generate_URL(self) -> str:
        """
        Generate the URL of the web request.
        
        Returns:
            str: URL of the web request.
        """
        pass

class JumboJSONGenerator(JSONGenerator):
    def __init__(self) -> None:
        self.page = 1

    def _found_categories(self, categories: list):
        """
        Process the categories for inclusion in the JSON key.
        
        Args:
            categories (list): list of categories.
            
        Returns:
            tuple: tuple with three lists:
                1. category mapping.
                2. Categories query.
                3. Selected facets.
        """
        map = []
        query = []
        selected_facets = []
        
        number_categories = len(categories)
        if number_categories != 1:
            for i in range(number_categories):
                map.append(f"category-{i + 1}")
                query.append(categories[i])
                if i == 0:
                    selected_facets.append("[{"f'"key": "category-{i + 1}", "value": "{categories[i]}"'+"}")
                elif number_categories == i + 1:
                    selected_facets.append("{"f'"key": "category-{i + 1}", "value": "{categories[i]}"'+"}]")
                else:
                    selected_facets.append("{"f'"key": "category-{i + 1}", "value": "{categories[i]}"'+"}")
        
        return map, query, selected_facets
    
    def generate_key(self, categories: list, page: int):
        """
        Generate the JSON key for the web request.
        
        Args:
            categories (list): List of categories.
            page (int): Page number.
            
        Returns:
            str: base64 encoded JSON key.
        """
        start, end = number_range(page)
        self.page = page
        map, query, selected_facets = self._found_categories(categories)
        json_format = '{"hideUnavailableItems":true,"skusFilter":"FIRST_AVAILABLE","simulationBehavior":"default","installmentCriteria":"MAX_WITHOUT_INTEREST","productOriginVtex":false,'+f'"map":"{",".join(map)}","query":"{"/".join(query)}","orderBy":"OrderByScoreDESC",'+f'"from":{start},"to":{end},'+f'"selectedFacets":{",".join(selected_facets)},'+'"facetsBehavior":"Static","categoryTreeBehavior":"default","withFacets":false,"showSponsored":false}'
        json_bytes = str.encode(json_format)
        content = base64.b64encode(json_bytes)
        key = content.decode()
        return key

class JumboURLCreator(URLCreator):
    def __init__(self) -> None:
        self.json_generator = JumboJSONGenerator()
    
    def generate_URL(self, categories: list, page: int) -> str:
        """
        Generate the URL of the web request.
        
        Args:
            categories (list): List of categories.
            page (int): Page number.
            
        Returns:
            str: URL of the web request.
        """
        key = self.json_generator.generate_key(categories, page)
        url= f"https://www.jumbo.com.ar/_v/segment/graphql/v1?workspace=master&maxAge=short&appsEtag=remove&domain=store&locale=es-AR&__bindingId=4780db52-b885-45f0-bbcc-8bf212bb8427&operationName=productSearchV3&variables=%7B%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22fd92698fe375e8e4fa55d26fa62951d979b790fcf1032a6f02926081d199f550%22%2C%22sender%22%3A%22vtex.store-resources%400.x%22%2C%22provider%22%3A%22vtex.search-graphql%400.x%22%7D%2C%22variables%22%3A%22{key}%3D%22%7D"
        return url

class JumboPriceSearching():
    def __init__(self) -> None:
        self.url_creator = JumboURLCreator()
        self.products = []

    def get_products(self):
        """
        Get the list of products.
        
        Returns:
            list: List of products.
        """
        return self.products

    async def extract_json(self, categories: list, session: aiohttp.ClientSession):
        """
        Extract the product data from the JSON obtained in the web request.
        
        Args:
            categories (list): list of categories.
            session (aiohttp.ClientSession): aiohttp session.
        """
        maximum_pages = 51 # Maximum number of pages that Jumbo website accepts.
        for i in range(1, maximum_pages):
            url = self.url_creator.generate_URL(categories, i)
            async with session.get(url) as response:
                if response.status == 200:
                    json_page = await response.json()

                    products = json_page.get("data", {}).get("productSearch", {}).get("products", [])
                    if not products:
                        if categories[2] == "":
                            print("FINALIZADO", categories[1])
                        else:
                            print("FINALIZADO", categories[2])
                        break

                    for product_data in products:
                        product_ID = product_data.get("productId")
                        product_name = product_data.get("productName")
                        product_price = product_data.get("priceRange", {}).get("sellingPrice", {}).get("highPrice")
                        if product_ID and product_name and product_price:
                            self.products.append([product_ID, product_name, categories[0], categories[1], categories[2], product_price, datetime.datetime.now().date()])
                else:
                    print(response.status)

class SQLite:
    def __init__(self, database_path) -> None:
        self.database_path = database_path
    
    def connect_db(self):
        return sqlite3.connect(self.database_path)

class SaveToCSVFromSQL(SQLite):
    def __init__(self, database_path) -> None:
        super().__init__(database_path)

    def save(self):
        """
        Save table data in CSV files.
        """
        for products in CONS_EVERYTHING:
            with self.connect_db() as conn:
                sql_query = pd.read_sql_query(
                    f"""
                    SELECT * FROM {products[0].CATEGORY}
                    """,
                    conn
                )

                df = pd.DataFrame(sql_query)
                df.to_csv(f"JumboBot/data/csv/{products[0].CATEGORY}.csv", index=False)

class SaveToSQL(SQLite):
    def __init__(self, price_searching, database_path) -> None:
        self.price_searching = price_searching
        super().__init__(database_path)
    
    def create_table(self, category: str, conn):
        cursor = conn.cursor()
        instruction = f"CREATE TABLE {category} (ID int, Product text, Category text, Subcategory text, Price int, Date text)"
        cursor.execute(instruction)
        cursor.close()

    def create_rows(self, ID: int, product: str, category: str, subcategories: str, subsubcategories:str, price: int, date: datetime):
        """
        Create rows in the corresponding table in the SQLite database.
        
        Args:
            ID (int): ID of the product.
            product (str): Product name.
            category (str): Product category.
            subcategories (str): Subcategory of the product.
            subsubcategories (str): Sub-subcategory of the product.
            price (int): Price of the product.
            date (datetime.datetime): Insertion date.
        """
        with self.connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{category}'")
            data = cursor.fetchall()

            if data == []:
                self.create_table(category, conn)

            cursor.execute(f"SELECT COUNT(*) FROM {category} WHERE id = ? AND date = ?", (ID, date))
            count = cursor.fetchall()[0]

            if int(count[0]) == 0:
                if "'" in product or '"' in product:
                    product = product.replace("'", "").replace('"', "")
                instruction = f"INSERT INTO {category} VALUES ({ID}, '{product}', '{subcategories}', '{subsubcategories}', {price}, '{date}')"
                cursor.execute(instruction)
                
            conn.commit()
            cursor.close()

    def save(self):
        """
        Save the product data in the SQLite database.
        """
        for product in self.price_searching.products:
            id, name, category, subcategory, subsubcategory, price, date = product
            self.create_rows(int(id), name, category, subcategory, subsubcategory, int(price), date)





class CalculatePorcentageSQL(SQLite):
    def __init__(self, database_path):
        super().__init__(database_path)

    def percentage(self, old_value, new_value):
        """
        Calculate the percentage of variation between two values.
        
        Args:
            old_value (float): old value.
            new_value (float): New value.
            
        Returns:
            tuple: Tuple with two elements:
                1. State of the variation (emoji and color).
                2. Variation percentage.
        """
        direction = None
        percentage = 0
        
        if old_value > new_value:
            percentage = 100 * ((old_value - new_value) / old_value) * -1
            direction = "⬇️🟢"
        elif old_value < new_value:
            percentage = 100 * ((new_value - old_value) / old_value)
            direction = "⬆️🔴"
        
        if percentage > 0 and percentage < 0.1:
            round_percentage = round(percentage, 3)
        else:
            round_percentage = round(percentage, 2)

        return direction, round_percentage

    def process_price_variation(self, product_price_variation, table):
        
        prices = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(list))))
        prices[table]["old_price"] = []
        prices[table]["new_price"] = []

        for product in product_price_variation:

            category, subcategory, old_price, new_price = product

            prices[table][category][subcategory]["old_price"].append(old_price)
            prices[table][category][subcategory]["new_price"].append(new_price)

            prices[table]["old_price"].append(old_price)
            prices[table]["new_price"].append(new_price)


        return prices

    def select_instruction(self, table, period_type: str, period_number: int):
        month_offset = ""
        match period_type.lower():
            case "days":
                date_offset = f"-{period_number} days"
            case "month":
                date_offset = "start of month"
                month_offset = f", '-{period_number} month'"
            case "year":
                raise NotImplementedError()


        instruction = f"""
        SELECT p2.category, p2.subcategory, p2.price, p1.price
            FROM {table} p2
            JOIN {table} p1 ON p2.id = p1.id 
            WHERE 
                p2.date = DATE('now', '{date_offset}'{month_offset}, '-3 hour') AND
                p1.date = DATE('now', '-1 day', '-3 hour')
            ORDER BY
                    p2.id"""
    
        return instruction

    def calculate_per_tables(self, table: str, period_type: str, period_number: int) -> list:
        with self.connect_db() as conn:
            cursor = conn.cursor()
            instruction = self.select_instruction(table, period_type, period_number)
            cursor.execute(instruction)
            products_with_price_variation = cursor.fetchall()
            prices = self.process_price_variation(products_with_price_variation, table)

            promedy_old_prices = sum(prices[table]["old_price"]) / len(prices[table]["old_price"])
            promedy_new_prices = sum(prices[table]["new_price"]) / len(prices[table]["new_price"])
            price_direction, percentage = self.percentage(promedy_old_prices, promedy_new_prices)
            category = f"{table.capitalize().replace('_', ' ')}"

            display_content = []
            if percentage != 0: 
                display_content.append({
                    "category": category,
                    "price_direction": price_direction,
                    "percentage": percentage
                })

        cursor.close()
        return display_content
    
    
    def calculate_per_subcategories(self, table, period_type: str, period_number: int):
        with self.connect_db() as conn:
            cursor = conn.cursor()
            instruction = self.select_instruction(table, period_type, period_number)
            cursor.execute(instruction)
            products_with_price_variation = cursor.fetchall()
            prices = self.process_price_variation(products_with_price_variation, table)

            display_content = []
            for category, subcategories, in prices[table].items():
                if category != "old_price" and category != "new_price":
                    for subcategory in subcategories:
                        promedy_old_prices = sum(prices[table][category][subcategory]["old_price"]) / len(prices[table][category][subcategory]["old_price"])
                        promedy_new_prices = sum(prices[table][category][subcategory]["new_price"]) / len(prices[table][category][subcategory]["new_price"])
                        
                        price_direction, percentage = self.percentage(promedy_old_prices, promedy_new_prices)
                        if percentage != 0: 
                            display_content.append({
                                "category": category,
                                "subcategory": subcategory,
                                "price_direction": price_direction,
                                "percentage": percentage
                            })

        cursor.close()
        return display_content

class ImpresionLogic():
    def __init__(self, calculator: CalculatePorcentageSQL) -> None:
        self.calculator = calculator

    def create_first_message(self, period_type: str, old_day: int = None, new_day: int = None, week_number: int = None, month: str = None, year: int = None) -> str:
        if period_type == "day":
            message = f"Variación de precios - {old_day} a {new_day} - {month} {year}:\r\n\r\n"
        elif period_type == "week":
            message = f"Variación de precios - Semana {week_number} - {month} {year}:\r\n\r\n"
        elif period_type == "month":
            message = f"Variación de precios - {month} {year}:\r\n\r\n"
        else:
            raise ValueError("Tipo de período no válido.")
        return message

    def create_messages_per_tables(self, period_type: str, number_days: int):
        """
        Create messages for the impression logic.
        
        Args:
            period_type (str): Type of period (day, week, month, year).
            number_days (int): Number of days.
        """
        messages = []
        used_categories = []
        for category in CONS_CATEGORIES:
            if not category in used_categories:
                used_categories.append(category)
                data_info = self.calculator.calculate_per_tables(category, period_type, number_days)
                if data_info != []:
                    messages.append(f"{data_info[0]['category'].capitalize() + select_emoji(category) + data_info[0]['price_direction']}{data_info[0]['percentage']}%")
        
        return messages

    def create_messages_per_subcategories(self, period_type: str, number_days: int):
        """
        Create messages for the impression logic.
        
        Args:
            period_type (str): Type of period (day, week, month, year).
            number_days (int): Number of days.
        """
        messages = []
        used_categories = []
        for category in CONS_CATEGORIES:
            if not category in used_categories:
                used_categories.append(category)
                data_info = self.calculator.calculate_per_subcategories(category, period_type, number_days)
                if data_info != []:
                    messages.append("\r\n" + category.capitalize() + select_emoji(category) + ":" + "\r")
                    for data in data_info:
                        if data["subcategory"] == "":
                            messages.append(f"{data['category'].capitalize() + data['price_direction']}{data['percentage']}%")
                        else:
                            messages.append(f"{data['subcategory'].capitalize() + data['price_direction']}{data['percentage']}%")

        return messages
    
    def create_top_messages(self, top_number: int, messages: list, mode: int):
        """
        Create top messages.
        
        Args:
            top_number (int): Number of top messages.
            messages (list): List of messages.
            mode (str): Mode of the messages (increases[0] or decreases[1]). 
        """
        if mode == 0:
            filtered_messages = filter(lambda x: "⬆️🔴" in x, messages)
        if mode == 1:
            filtered_messages = filter(lambda x: "⬇️🟢" in x, messages)

        key = lambda x: extract_number(x[-7:]) # The number "-7" is for optimization, means that in the last 7 characters of the string, there is a number.

        sorted_messages = sorted(filtered_messages, key=key, reverse=True)

        if len(sorted_messages) > top_number:
            return sorted_messages[:top_number]
    
        return sorted_messages[:len(sorted_messages)]


    def print_products(self, old_day, new_day):
        pass        

class TwitterLogic():
    def __init__(self) -> None:
        self.client = None
    
    def connect_twitter(self):
        """
        Connect to Twitter.
        """
        json_tokens = read_tokens()
        self.client = tweepy.Client(
            json_tokens["bearer_token"],
            json_tokens["API_key"],
            json_tokens["API_key_secret"],
            json_tokens["access_token"],
            json_tokens["access_token_secret"])

    def send_tweet(self, text: str, in_reply_to_tweet_id: int = None):
        """
        Send a tweet.
        
        Args:
            text (str): Text of the tweet.
            in_reply_to_tweet_id (int): ID of the tweet to reply to.
        """
        if in_reply_to_tweet_id == None:
            response = self.client.create_tweet(text=text)
        else:
            response = self.client.create_tweet(in_reply_to_tweet_id=in_reply_to_tweet_id, text=text)

class App:
    def __init__(self, price_searching, save_to: SaveToSQL, calculator: CalculatePorcentageSQL) -> None:
        self.price_searching = price_searching
        self.save_to = save_to
        self.calculator = calculator
    
    # This function is used to extract the data from the Jumbo website.
    async def async_search_prices(self):
        my_conn = aiohttp.TCPConnector(limit=20)
        async with aiohttp.ClientSession(connector=my_conn) as session:
            tasks = []
            for products in CONS_EVERYTHING:
                for categories in products:
                    category = categories.CATEGORY
                    subcategory = categories.SUBCATEGORY
                    subsubcategory = categories.SUBSUBCATEGORY
                    task = asyncio.create_task(self.price_searching.extract_json(categories=[category, subcategory, subsubcategory], session=session))
                    tasks.append(task)
            await asyncio.gather(*tasks, return_exceptions=True)
    
    def save(self, *args):
        """
        Args:
            *args: aditional space to saves
        """
        self.save_to.save()
        if not args == None:
            for arg in args:
                arg.save()

    def print_messages(self, messages: list):
        for message in messages:
            print(message.replace("_", " "))


def main():
    SQL_path = "JumboBot/data/products.db"

    price_searching = JumboPriceSearching()
    SQL_save = SaveToSQL(price_searching, SQL_path)
    calculator = CalculatePorcentageSQL(SQL_path)
    impression_logic = ImpresionLogic(calculator)
    app = App(price_searching, SQL_save, calculator)

    # I use the loop twice to make sure the data is saved in the database.

    for _ in range(2):
        asyncio.run(app.async_search_prices())
        app.save()
     
    messages_per_table = impression_logic.create_messages_per_tables("days", 1)
    messages_per_subcategory = impression_logic.create_messages_per_subcategories("days", 1)

    app.print_messages(messages_per_table)
    app.print_messages(messages_per_subcategory)

if "__main__" == __name__:
    main()



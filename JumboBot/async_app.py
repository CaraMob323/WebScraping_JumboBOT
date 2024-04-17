import requests
import base64
import sqlite3
import datetime
import sqlite3
import pandas as pd
import asyncio
import aiohttp
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
        self.json_generator = json_generator

    @abstractmethod
    def generate_URL(self) -> str:
        pass

class PriceSearching(ABC):
    @abstractmethod
    def __init__(self) -> None:
        self.products = {}

class JumboJSONGenerator(JSONGenerator):
    def __init__(self) -> None:
        self.page = 1

    def _found_categories(self, categories: list):
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
        key = self.json_generator.generate_key(categories, page)
        url= f"https://www.jumbo.com.ar/_v/segment/graphql/v1?workspace=master&maxAge=short&appsEtag=remove&domain=store&locale=es-AR&__bindingId=4780db52-b885-45f0-bbcc-8bf212bb8427&operationName=productSearchV3&variables=%7B%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22fd92698fe375e8e4fa55d26fa62951d979b790fcf1032a6f02926081d199f550%22%2C%22sender%22%3A%22vtex.store-resources%400.x%22%2C%22provider%22%3A%22vtex.search-graphql%400.x%22%7D%2C%22variables%22%3A%22{key}%3D%22%7D"
        return url

class JumboPriceSearching(PriceSearching):
    def __init__(self) -> None:
        self.url_creator = JumboURLCreator()
        self.products = []

    def get_products(self):
        return self.products

    async def extract_json(self, categories: list, session: aiohttp.ClientSession):
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
    def __init__(self, price_searching: PriceSearching, database_path) -> None:
        self.price_searching = price_searching
        super().__init__(database_path)
    
    def create_table(self, category: str, conn):
        cursor = conn.cursor()
        instruction = f"CREATE TABLE {category} (ID int, Product text, Category text, Subcategory text, Price int, Date text)"
        cursor.execute(instruction)
        cursor.close()

    def create_rows(self, ID: int, product: str, category: str, subcategories: str, subsubcategories:str, price: int, date: datetime):
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
        for product in self.price_searching.products:
            id, name, category, subcategory, subsubcategory, price, date = product
            self.create_rows(int(id), name, category, subcategory, subsubcategory, int(price), date)


class CalculatePorcentageSQL(SQLite):
    def __init__(self, database_path):
        super().__init__(database_path)

    def porcentage(self, old_value, new_value):
        if old_value > new_value:
            porcentage = 100 * ((old_value - new_value) / old_value)
            status = "⬇️🟢-"
        elif old_value < new_value:
            porcentage = 100 * ((new_value - old_value) / old_value)
            status = "⬆️🔴+"
        else:
            status = None
            porcentage = None
                
        return status, porcentage

    def process_price_variation(self, product_price_variation, table):
        prices = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(list))))

        for product in product_price_variation:

            category, subcategory, old_price, new_price = product

            prices[table][category][subcategory]["old_price"].append(old_price)
            prices[table][category][subcategory]["new_price"].append(new_price)

        return prices

    def calculate_per_day(self, table):
        with self.connect_db() as conn:
            cursor = conn.cursor()
            instruction = f"""
            SELECT p2.category, p2.subcategory, p2.price, p1.price
            FROM {table} p2
            JOIN {table} p1 ON p2.id = p1.id 
            WHERE 
                p2.date = DATE('now', '-1 day') AND
                p1.date > DATE('now', '-1 day')
            ORDER BY
                    p2.id,
                    p1.date,
                    p2.date"""
                

            cursor.execute(instruction)
            products_with_price_variation = cursor.fetchall()
            prices = self.process_price_variation(products_with_price_variation, table)

            today = datetime.datetime.now().date()
            yesterday = today - datetime.timedelta(days=1)

            messages = []
            for category, subcategories, in prices[table].items():
                for subcategory in subcategories:
                    promedy_old_prices = sum(prices[table][category][subcategory]["old_price"]) / len(prices[table][category][subcategory]["old_price"])
                    promedy_new_prices = sum(prices[table][category][subcategory]["new_price"]) / len(prices[table][category][subcategory]["new_price"])
                    
                    status, porcentage = self.porcentage(promedy_old_prices, promedy_new_prices)
                    if not status == None:
                        messages.append([id, category, subcategory, status, porcentage, yesterday, today])

        cursor.close()
        return messages
            
class App:
    def __init__(self, price_searching: PriceSearching, save_to: SaveToSQL, calculator: CalculatePorcentageSQL) -> None:
        self.price_searching = price_searching
        self.save_to = save_to
        self.calculator = calculator
        
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
        Parameters:
            *args: aditional space to saves
        """
        self.save_to.save()
        if not args == None:
            for arg in args:
                arg.save()
    
    def impression_logic(self):
        used_categories = []
        for products in CONS_EVERYTHING:
            for categories in products:
                category = categories.CATEGORY
                if not category in used_categories:
                    messages = self.calculator.calculate_per_day(category)
                    if not messages == []:
                        print(category.capitalize())
                    for message in messages:
                        id, subcategory, subsubcategory, status, porcentage, yesterday, today = message
                        if subsubcategory == "":
                            print(f"{subcategory} {status}{round(porcentage, 2)}% ")
                        else:
                            print(f"{subsubcategory} {status}{round(porcentage, 2)}% ")
                    used_categories.append(category)

def main():
    SQL_path = "JumboBot/data/products.db"

    price_searching = JumboPriceSearching()
    SQL_save = SaveToSQL(price_searching, SQL_path)
    CSV_save = SaveToCSVFromSQL(SQL_path)
    calculator = CalculatePorcentageSQL(SQL_path)
    app = App(price_searching, SQL_save, calculator)
    # asyncio.run(app.async_search_prices())
    app.save()
    app.impression_logic()

if "__main__" == __name__:
    main()
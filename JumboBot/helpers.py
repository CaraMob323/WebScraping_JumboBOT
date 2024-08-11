import json
from re import findall

# Really I don't know why I need this function, but it's needed.
def number_range(number):
    start = (number - 1) * 20 + 1
    end = start + 19
    return start - 1, end - 1

def select_emoji(category: str):
    categories =  {
        'electro': "🔌",
        'hogar y textil': "🪑",
        'tiempo libre': "🏡",
        'bebes y niños': "👶",
        'almacen': "🥫",
        'bebidas': "🍷",
        'frutas y verduras': "🥕",
        'carnes': "🥩",
        'lacteos': "🥛",
        'quesos y fiambres': "🧀",
        'congelados': "❄️",
        'panadería y repostería': "🥖",
        'comidas preparadas': "🍽",
        'perfumeria': "🧴",
        'limpieza': "🧹"
        }
    
    return categories[category.lower().replace("_", " ")]

def read_tokens():
    with open("token_x.json", "r") as file:
        return json.load(file)

def extract_number(text: str):
    """
    Extract a number from a string.
    
    Args:
        text (str): Text to extract the number from.
        
    Returns:
        float: Number extracted from the text.
    """
    number = findall(r'\d+\.\d+', text)
    if number:
        return float(number[0])
    return None
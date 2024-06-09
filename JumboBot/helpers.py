import json

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
        'perfumeria': "🧴"
        }
    
    return categories[category.lower()]

def read_tokens():
    with open("token_x.json", "r") as file:
        return json.load(file)

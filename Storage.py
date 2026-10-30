import json
from pathlib import Path

FILE_PATH = Path(__file__).parent / "countries.json"

def load_countries():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_country(code, data):
    countries = load_countries()
    countries[code] = data

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(countries, file, indent=4, ensure_ascii=False)

def get_saved_country(code):
    countries = load_countries()
    return countries.get(code)
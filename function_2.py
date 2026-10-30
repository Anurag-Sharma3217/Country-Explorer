import requests, Utils as ut

def fetch_country(code):
    url = f"https://countries.dev/alpha/{code}"

    country = requests.get(url, timeout=10)
    print(country.status_code)
    country.raise_for_status()
    return country.json()


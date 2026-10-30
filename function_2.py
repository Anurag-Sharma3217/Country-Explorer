import requests, Utils as ut

def fetch_country(code):
    url = f"https://countries.dev/alpha/{code}"

    country = requests.get(url, timeout=10)
    print(country.status_code)
    country.raise_for_status()
    return country.json()

def display_data():
    try:
        data = fetch_country()
        print("\nCountry name:", data.get("name", "Not available"))
        print("\nCountry capital:", data.get("capital", "Not available"))
        print("\nCountry population:", data.get("population"))
    
        print("\nCountry Currency Information")
        for info in data.get("currencies", "Not available"):
            for currency in info:
                print(f"{currency}: {info.get(currency, 'Not available')}")
        
        print("\nCountry language information")
        for info in data.get("languages", "Not available"):
            for language in info:
                print(f"{language}: {info.get(language, 'Not available')}")

    except requests.ConnectionError:
        print("Could not connect. Check your connection.")

    except requests.ConnectTimeout:
        print("The request timed out. Try again.")

    except requests.JSONDecodeError as error:
        print(f"Json decoding fail: {error}")

    except requests.HTTPError as error:
        print(f"HTTP error: {error}")

    except requests.RequestException as error:
        print(f"Request failed: {error}")
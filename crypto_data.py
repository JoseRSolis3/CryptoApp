import requests

def get_crypto_price(crypto="bitcoin", currency="usd"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}"
    response = requests.get(url)
    data = response.json()

    if crypto not in data:
        return "Error: crypto not in data"

    price = data[crypto][currency]
    formatted_price = "{:.20f}".format(price).rstrip('0').rstrip('.')

    return formatted_price
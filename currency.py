import json
import requests

currencies: dict = None

def exchange(quantity: float, current_currency, convert_currency):
    
    curr_value = get_currency_value(current_currency, convert_currency)
    return curr_value * quantity

def get_all_curr():
    global currencies
    if currencies is None:
        resource = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json")
        str_data = resource.text
        currencies = json.loads(str_data)
    return currencies


def get_currency_value(current_curr, convert_curr) -> float:
    resource = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/"
    resource += current_curr + "/" + convert_curr + ".json"
    #response
    resp = requests.get(resource).text
    value: dict = json.loads(resp)
    return value.get(convert_curr)

def is_valid(currency: str):
    currencies = get_all_curr()
    if currencies.get(currency) is not None:
        return True
    return False



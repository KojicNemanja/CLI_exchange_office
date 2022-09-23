import json
import requests
import errors

currencies: dict = None

def exchange()->float:
    quantity = float(input("Enter quantity -> "))
    is_qiantity_valid(quantity)
    current_currency = input("Enter current currency -> ")
    is_curr_valid(current_currency)
    convert_currency = input("Enter convert currency -> ")
    is_curr_valid(convert_currency)
    data = get_currency_data(current_currency, convert_currency)
    currency_value = data[convert_currency]
    date = data['date']
    s = "On date: {}\ncurrency value: {}\ntotal: {:.2f}".format(date, currency_value, (currency_value * quantity))
    print(s)

def get_all_curr():
    global currencies
    if currencies is None:
        resource = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json")
        str_data = resource.text
        currencies = json.loads(str_data)
    return currencies
    

def get_currency_data(current_curr, convert_curr) -> float:
    resource = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/"
    resource += current_curr + "/" + convert_curr + ".json"
    #response
    resp = requests.get(resource).text
    return json.loads(resp)

def is_qiantity_valid(quantity: float):
    if quantity < 0:
        raise errors.QuantityNotEnough(quantity)

def is_curr_valid(currency: str):
    currencies = get_all_curr()
    if currencies.get(currency) is None:
        raise errors.InvalidCurrency(currency)






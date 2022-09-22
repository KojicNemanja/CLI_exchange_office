from currency import exchange


try:
    quantity = float(input("Enter quantity -> "))
    current_currency = input("Enter current currency -> ")
    convert_currency = input("Enter convert currency -> ")
    print(exchange(quantity, current_currency, convert_currency))
except Exception as ex:
    print(ex)

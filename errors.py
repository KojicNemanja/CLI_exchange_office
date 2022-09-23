class InvalidCurrency(Exception):
    def __init__(self, currency, message = "Entered currency isn't valid!"):
        super().__init__(message)
        self.currency = currency
        self.message = message
    
    def __str__(self):
        return f'*{self.currency} -> {self.message}'


class QuantityNotEnough(Exception):
    def __init__(self, quantity, message = "Quantity must be greater than zero!"):
        super().__init__(message)
        self.quantity = quantity
        self.message = message

    def __str__(self):
        return f'*{self.quantity} -> {self.message}'
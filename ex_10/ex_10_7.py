class Element:
    def __init__(self, name,symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return f'name={self.name}, symbol={self.symbol}, number={self.number}'
h_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**h_dict)
print(hydrogen)
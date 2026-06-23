h_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
hydrogen = Element(**h_dict)
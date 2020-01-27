class Element():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self):
        return self.__name
    def symbol(self):
        return self.__symbol
    def number(self):
        return self.__number
    @name.setter
    def name(self, input_name):
        self.__name = input_name
    @symbol.setter
    def symbol(self, input_symbol):
        self.__symbol = input_symbol
    @number.setter
    def number(self, input_number):
        self.__number = input_number
    def __str__(self):
        return self.name

element_dict = {'name' : 'Hydrogen', 'symbol' : 'H', 'number' : 1}

"""
class dump():
    def __init__(self, element):
        self.ele = element
    def detail(self):
        print('Name: ', self.ele.name)
        print('Symbol: ', self.ele.symbol)
        print('Number: ', self.ele.number)
"""

hydrogen = Element('Hydrogen', 'H', 1)

print(hydrogen)
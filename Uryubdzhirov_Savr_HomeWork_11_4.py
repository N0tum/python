class Storage:
    def __init__(self):
        self._dict = {}

    def add(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Equipment:
    def __init__(self, name, quantity, year):
        self.name = name
        self.quantity = quantity
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.quantity} {self.year}'


class Printer(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def __repr__(self):
        return f'{self.name} {self.quantity} {self.year}'

    def action(self):
        return 'Printing'


class Scanner(Equipment):

    def action(self):
        return 'Scanning'


class Copier(Storage):

    def action(self):
        return 'Copies'


Store = Storage()
scan1 = Scanner('hp', 321, 2019)
Store.add(scan1)
scan2 = Scanner('Cannon', 330, 2014)
Store.add(scan2)
printer = Printer('Sony', 40, 2018)
Store.add(printer)
print(Store._dict)


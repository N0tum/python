class Warehouse:

    def __init__(self, name, quantity, numb, *args):
        self.name = name
        self.quantity = quantity
        self.numb = numb
        self.store_full = []
        self.store = []
        self.new_unit = {'model': self.name, 'quantity': self.quantity}

    def __str__(self):
        return f'{self.name} : {self.quantity}'

    def obtain(self):

        try:
            unit = input(f'Enter a model: ')
            unit_q = int(input(f'Enter a quantity: '))
            unique = {'model': unit, 'quantity': unit_q}
            self.new_unit.update(unique)
            self.store.append(self.new_unit)
            print(f'{self.store}')
        except:
            return f'Error'

        print(f'Do you want to complete the process?')
        q = input(f'Print y or skip: ')
        if q == 'y':
            self.store_full.append(self.store)
            print(f'{self.store_full}')
            return f'Bye!'
        else:
            return Warehouse.obtain(self)


class Printer(Warehouse):
    def to_print(self):
        return f'to print {self.numb} times'


class Scanner(Warehouse):
    def to_scan(self):
        return f'to scan {self.numb} times'


class Copier(Warehouse):
    def to_copier(self):
        return f'to copier {self.numb} times'


unit_1 = Printer('HP', 5, 1)
unit_2 = Scanner('Canon', 5, 2)
unit_3 = Copier('Xerox', 1, 13)
print(unit_1.obtain())
print(unit_2.obtain())
print(unit_3.obtain())
print(unit_1.to_print())
print(unit_3.to_copier())

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self,  name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Full Name: {self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())



res = Position('Dante', 'Alighieri', 'poet', 3500, 1000)
print(res.get_full_name())
print(f'Total income: {res.get_total_income()}')
print(res.get_full_name())
print(f'Total income: {res.get_total_income()}')
print(res.position)
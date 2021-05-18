import time


class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def extract(cls, ex_date):
        result = list(map(int, ex_date.split('-')))
        return result

    @staticmethod
    def valid(va_date):
        try:
            time.strptime(va_date, '%d-%m-%Y')
            return 'Correct date!'
        except (ValueError, TypeError):
            return 'Wrong date!'


date = Date('11-1-2001')
print(date)
print(Date.valid("26-09-1996"))
print(date.valid("11-13-2011"))
print(Date.extract('30-04-1325'))
print(date.extract('11-11-1111'))

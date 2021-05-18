class DivisionByNull:

    @staticmethod
    def check(num1, num2):
        try:
            return (num1 / num2)
        except ZeroDivisionError:
            return (f"Division by zero!")


div = DivisionByNull()
print(DivisionByNull.check(99, 0))
print(DivisionByNull.check(30, 0.1))
print(div.check(47, 0))

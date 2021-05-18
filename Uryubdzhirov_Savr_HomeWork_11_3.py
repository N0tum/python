class Error:
    def __init__(self, *args):
        self.lis = []

    def input(self):

        while True:
            try:
                val = int(input('Enter the number:'))
                self.lis.append(val)
                print(f'{self.lis} \n ')
            except ValueError:
                print(f"Error! \nTry again?")
                choice = input(f'y/n: ')

                if choice == 'y':
                    print(err.input())
                else:
                    return f"{self.lis} \nBye!"
                    break


err = Error()
print(err.input())

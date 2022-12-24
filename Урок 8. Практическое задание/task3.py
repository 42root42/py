class MyValueExcept(Exception):
    def __init__(self, message):
        self.message = message


num_list = []
while True:
    i = input('Введите число(для завершения ввода просто Enter): ')
    if i != '':
        try:
            if not i.isnumeric():
                raise MyValueExcept('Введено не число!')
        except MyValueExcept as error:
            print(error)
        else:
            num_list.append(i)
    else:
        break

print(num_list)

class Zeroing(Exception):
    def __init__(self, message):
        self.message = message


num_1 = int(input('Введи первое число: '))
num_2 = int(input('Введи второе число(делитель): '))


try:
    if num_2 == 0:
        raise Zeroing('Делить на 0 нельзя')
except Zeroing as error:
    print(error)
else:
    result = num_1 / num_2
    print(f'{num_1} / {num_2} = {result}')

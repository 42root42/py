class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.с = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма:')
        return f'с = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение:')
        return f'с = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'с = {self.a} + {self.b} * i'


num_1 = ComplexNumber(4, 2)
num_2 = ComplexNumber(7, -1)
print(num_1)
print(num_1 + num_2)
print(num_1 * num_2)

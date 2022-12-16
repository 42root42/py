class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return self.quantity - other.quantity
        else:
            return f'Отрицательное значение: не выполнено'

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def make_order(self, val):
        res = '| '
        for i in range(int(self.quantity / val)):
            res += "*" * val + '\n| '
        res += f'{"*" * (self.quantity % val)}'
        return res


cell1 = Cell(12)
cell2 = Cell(5)

cell3 = Cell(15)
cell4 = Cell(5)

print('+------------------------------+')

print(f'| Сложение = {cell1 + cell2}')

print('+------------------------------+')

print(f'| Вычитание раз = {cell2 - cell1}')
print(f'| Вычитание два = {cell3 - cell4}')

print('+------------------------------+')

print(f'| Умножение = {cell1 * cell2}')

print('+------------------------------+')

print(f'| Деление = {cell1 / cell2}')

print('+------------------------------+')

print("| По рядам:")
print(cell1.make_order(5))
print(cell2.make_order(10))

print('+------------------------------+')

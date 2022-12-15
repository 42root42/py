class Stationery:
    title: str

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationery):
    def draw(self):
        return f'Начинаем рисовать ручкой'


class Pencil(Stationery):
    def draw(self):
        return f'Отрисовка карандашом'


class Handle(Stationery):
    def draw(self):
        return f'Рисуем маркером'


ans = input('Чем хочешь рисовать(ручка, карандаш или маркер)? ')
if ans == 'ручка':
    print(Pen().draw())
elif ans == 'карандаш':
    print(Pencil().draw())
else:
    print(Handle().draw())

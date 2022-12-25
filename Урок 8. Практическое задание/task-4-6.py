class Store:

    def __init__(self, name, price, amount, power):
        self.name = name
        self.price = price
        self.amount = amount
        self.power = power
        self.my_store_all = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена': self.price,
                        'Количество': self.amount}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.amount}'

    def reception(self):
        try:
            unit = input('Введите название/модель: ')
            unit_p = int(input('Цена: '))
            unit_q = int(input('Количество: '))
            unique = {'Модель устройства': unit, 'Цена': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий прайслист: -\n {self.my_store}')
            out = input('Для выхода нажмите "q" ')
            if out == 'q':
                self.my_store_all.append(self.my_store)
                print(f'Все товары -\n {self.my_store_all}')
                return 'До новых встреч'

            else:
                return Store.reception(self)

        except:
            return 'Ошибка ввода данных'


class Printer(Store):
    def to_print(self):
        return f'кол-во потребляемой энергии кВт/ч {self.power}'


class Scanner(Store):
    def to_scan(self):
        return f'кол-во потребляемой энергии кВт/ч {self.power}'


class Copier(Store):
    def to_copier(self):
        return f'кол-во потребляемой энергии кВт/ч {self.power}'


num_1 = Printer('Принтер', 400, 1, 4)
num_2 = Scanner('Сканер', 200, 2, 12)
num_3 = Copier('Ксерокс', 600, 3, 10)
num_1.reception()

class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus
        }


class Position(Worker):
    def get_full_name(self):
        return f'{self.position} {self.name} {self.surname} получает:'

    def get_total_income(self):
        return sum(self._income.values())


ename, esurname, eposition, ewage, ebonus = input('Введи Имя, Фамилию, Должность, Оклад и премию: ').split()

employee = Position(ename, esurname, eposition, int(ewage), int(ebonus))
print(employee.get_full_name(), employee.get_total_income())

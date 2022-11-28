a = int(input('Введите результат первого дня: '))
b = int(input('Сколько километров нужно:'))

days = 1

while a < b:
    a = a + (a * 0.1)
    days += 1

print(f'Номер дня: {days}')

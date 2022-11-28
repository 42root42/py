revenue = int(input('Введите выручуу фирмы: '))
costs = int(input('Введите издержки фирмы: '))

if revenue > costs:
    print('Фирма работает в прибыль')
    
    profit = revenue / costs
    print(f'Рентабельность равна {profit}')
          
    employee = int(input('Сколько сотрудников в фирме? '))
    p2e = revenue / employee
    print(f'Прибыль на одного сортудника составляет: {p2e}')

else:
    print('Фирма работает в убыток')

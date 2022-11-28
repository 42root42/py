revenue = int(input('Введите выручуу фирмы: '))
costs = int(input('Введите издержки фирмы: '))

if revenue > costs:
    print('Фирма работает в прибыль')

elif revenue == costs:
    print('Фирма работает в ноль')
    
else:
    print('Фирма работает в убыток')

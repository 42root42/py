a = []

while True:
    x = input('Введи элемент в список или stop, если уже достаточно: ')
    if x == 'stop':
        break
    a.append(x)

for el in range(0, len(a)-1, 2):
    a[el], a[el+1] = a[el+1], a[el]

print(a)
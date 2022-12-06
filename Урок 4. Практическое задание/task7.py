from math import factorial


def fact(n):
    for i in range(n):
        print(i, end='! = ')
        yield factorial(i)


n = int(input('До какого числа выводить n!: ')) + 1

for el in fact(n):
    print(el)

def my_func(d, e, f):
    n_list = [d, e, f]
    n_list.sort()
    print(n_list[-2] + n_list[-1])


a = int(input('Введи первое число: '))
b = int(input('Введи второе число: '))
c = int(input('Введи третье число: '))

my_func(a, b, c)

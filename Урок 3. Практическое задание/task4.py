def my_func(x, y):
    result = 1

    for i in range(abs(y)):
        result *= x

    if y >= 0:
        return result
    else:
        return 1 / result


n = float(input('Введи действительное положительное число: '))
m = int(input('Введи целое отрицательное число: '))

print(my_func(n, m))

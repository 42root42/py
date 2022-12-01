def dev_func(x, y):
    try:
        result = x / y

    except ZeroDivisionError:
        return "На ноль делить нельзя"

    return result


num_1, num_2 = int(input('Введи первое число: ')), int(input('Введи второе число и мы их поделим: '))

print(dev_func(num_1, num_2))

def sum_func():
    result = 0
    finish = False

    while not finish:
        usr_str = input('Введи числа через пробел или введи f для остановки: ').split()

        int_res = 0
        for i in range(len(usr_str)):
            if usr_str[i] == 'f':
                finish = True
                break
            else:
                int_res = int_res + int(usr_str[i])

        result = result + int_res

        print(f'Текущая сумма = {result}')

    print(f'Итоговая сумма всех введенных чисел = {result}')


sum_func()
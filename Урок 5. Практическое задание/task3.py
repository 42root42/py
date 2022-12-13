with open('files/task3.txt', 'r', encoding='UTF-8') as f:
    salary = []
    survive = []

    lst = f.read().split('\n')

    for l in lst:
        l = l.split()

        if float(l[1]) < 20000:
            survive.append(l[0])

        salary.append(l[1])

    av_sal = sum(map(float, salary)) / len(salary)

print(f'Выживают на грани(оклад меньше 20к): {survive}, \n Средняя зарплата по больничке: {av_sal} ')

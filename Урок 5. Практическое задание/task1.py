with open('files/task1.txt', 'w', encoding='UTF-8') as f:
    while True:
        userinput = input('Вводи данные, а когда надоест, отправь пустую строку: ')
        if userinput == '':
            break
        else:
            f.write(userinput + '\n')

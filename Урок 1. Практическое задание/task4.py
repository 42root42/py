number = int(input('Введи целое положительное число: '))

x = number % 10
number = number // 10

while number > 0:
    if number % 10 > x:
        x = number % 10

    number = number // 10
    
print(x)

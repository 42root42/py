def pers_data(**kwargs):
    print(f"Имя: {kwargs['name']}, Фамилия: {kwargs['surname']}, Год рождения: {kwargs['year']}, "
          f"Город: {kwargs['city']}, email: {kwargs['email']},Телефон: {kwargs['phone']}")

    """ Не лучшее применение вывода kwargs, но для теста вхождения параметров сойдет
    или просто print(kwargs)
    """


name = input('Введи имя: ')
surname = input('Фамилию: ')
year = int(input('Год рождения: '))
city = input('Город: ')
email = input('email: ')
phone = int(input('Телефон: '))

pers_data(name=name, surname=surname, year=year, city=city, email=email, phone=phone)

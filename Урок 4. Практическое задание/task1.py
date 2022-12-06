from sys import argv

script_name, emp, rate, hours, bonus = argv


def pay(rate, hours, bonus):
    try:
        if int(hours) > 200:
            print(f'{emp} поработал хорошо, поэтому зп с премией составила {int(rate) * int(hours) + int(bonus)} баксов')
        else:
            print(f'{emp} заработал {int(rate) * int(hours)} баксов')

    except:
        print('Что-то пошло не так')


pay(rate, hours, bonus)

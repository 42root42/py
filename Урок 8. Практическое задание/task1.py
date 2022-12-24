class Data:
    day = 0
    month = 0
    year = 0

    day_month_year = '19-122-2022'

    @classmethod
    def parse(cls):
        cls.day = int(cls.day_month_year.split('-')[0])
        cls.month = int(cls.day_month_year.split('-')[1])
        cls.year = int(cls.day_month_year.split('-')[2])

        print(f'Введенная дата {cls.day} число, {cls.month} месяц, {cls.year} год')

    @staticmethod
    def validate(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return 'Дата указана верно'
                else:
                    return 'Не верно указан год'
            else:
                return 'Не верно указан месяц'
        else:
            return 'Не верно указан день'


Data.parse()
print(Data.validate(Data.day, Data.month, Data.year))

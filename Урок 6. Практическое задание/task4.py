class Car:
    speed: int
    color: str
    name: str
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str) -> None:
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'Автомобиль {self.name} поехал')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction: str):
        print(f'{self.name} направляется {direction}')

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Внимание! {self.name} превышает!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Внимание! {self.name} превышает!')


class PoliceCar(Car):
    is_police: bool = True


cars = [
    SportCar(180, 'Баклажан', 'Лада'),
    TownCar(82, 'Красная', 'Ока'),
    WorkCar(90, 'Черная', 'Волга'),
    PoliceCar(120, 'Белый', 'Патриот'),
]

for car in cars:
    car.go()
    car.show_speed()
    if car.name == 'Волга':
        car.turn('на улицу Громозеки')
    car.stop()
    print('-------')

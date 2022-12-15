from time import sleep


class TrafficLight:
    __color = {'Красный': 7, 'Жёлтый': 2, 'Зелёный': 5}

    def running(self):
        for key, value in TrafficLight.__color.items():
            print(key)
            sleep(value)


signal = TrafficLight()
signal.running()

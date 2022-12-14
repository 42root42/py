class Road:
    mass = 25
    thickness = 0.001

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

        res = _length * _width * Road.mass * Road.thickness

        print(f'Необходимо {res} тонн асфальта')


l = int(input('Введи длину дороги: '))
w = int(input('Введи ширину дороги: '))

a = Road(l, w)

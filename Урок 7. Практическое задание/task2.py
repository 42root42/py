from abc import abstractmethod, ABC


class Abs(ABC):
    @abstractmethod
    def calculation(self):
        pass


class Clothes(Abs):
    def __init__(self, topcoat_size, suite_growth):
        self.v = topcoat_size / 6.5 + 0.5
        self.h = 2 * suite_growth + 0.3

    @property
    def calculation(self):
        return self.v + self.h


consumption = Clothes(12, 11)

print(consumption.calculation)

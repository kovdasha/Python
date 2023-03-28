"""
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""

import math

class Road:
    mass_of_asphalt = 25
    thickness = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass_calc(self):
        return self._length * self._width * self.mass_of_asphalt * \
            self.thickness

length_input = int(input('Введите длину дороги: '))
width_input = int(input('Введите ширину дороги: '))
r = Road(length_input, width_input)
print(f'Для покрытия всего дорожного полотна необходимо {math.ceil(r.asphalt_mass_calc() / 1000)} тонн')
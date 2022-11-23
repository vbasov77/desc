"""
Задание 2.
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

class NonNegative:

    # def __get__(self, instance, owner):
    #     return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    # def __delete__(self, instance):
    #     del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        # owner - владелец атрибута - <class '__main__.Worker'>
        # my_attr - имя атрибута владельца
        self.my_attr = my_attr


class Road:
    length = NonNegative()
    width = NonNegative()
    _thickness_canvas = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_asphalt_masses(self, thickness):
        try:
            return (self._length * self._width * thickness * self._thickness_canvas)
        except TypeError:
            return None


# result = int(obj.get_asphalt_masses(25))
#
# print(f'Масса составит: {result} кг = {int(result / 1000)} тонн')

obj = Road(10, 10)
print(int(obj.get_asphalt_masses(25)))

obj.length = -10
obj.width = 10
print(int(obj.get_asphalt_masses(25)))




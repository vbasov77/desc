"""Добавим Метакласс к одной из прошлых задач, проверяющий наличие строк документации
в подконтрольном классе"""

class DocMeta(type):
    """Метакласс, проверяющий наличие строк документации в подконтрольном классе"""

    def __init__(self, clsname, bases, clsdict):
        # К моменту начала работы метода __init__ метакласса
        # словарь атрибутов контролируемого класса уже сформирован.
        for key, value in clsdict.items():
            # Пропустить специальные и частные методы
            if key.startswith("__"):
                continue

            # Пропустить любые невызываемые объекты
            if not hasattr(value, "__call__"):
                continue

            # Проверить наличие строки документирования
            if not getattr(value, "__doc__"):
                #print(value)
                raise TypeError(f"Метод {key} должен иметь строку документации")

        type.__init__(self, clsname, bases, clsdict)

class NonNegative:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        # owner - владелец атрибута - <class '__main__.Worker'>
        # my_attr - имя атрибута владельца
        self.my_attr = my_attr


class Road(metaclass=DocMeta):
    length = NonNegative()
    width = NonNegative()
    _thickness_canvas = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_asphalt_masses(self, thickness):
        # "!"
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




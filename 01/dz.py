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


class Worker:
    wage = NonNegative()
    bonus = NonNegative()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_salary(self):
        return self.wage + self.bonus


OBJ = Worker('Иван', 'Иванов','Программист', 100000, 10000)
print(OBJ.get_salary())

OBJ.wage = 100000
OBJ.bonus = -10000
print(OBJ.get_salary())


OBJ = Worker('Иван', 'Иванов', 'Программист', 100000, 10000)
print(OBJ.get_salary())

OBJ.wage = 100000
OBJ.bonus = 10000
print(OBJ.get_salary())


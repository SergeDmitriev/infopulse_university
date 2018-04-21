# OOP

# class Person:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self._age = age
#         self.__salary = salary
#
#     desc = {'title': 'Person'}
#
#     def set_name(self, name, surname):
#         self.full_name = [name, surname]
#
#
# p = Person('Serge', 24)
# print(p.name)
# print(p._age)  #скрыть из IDE
# # print(p.salary)  #скрыть и переименовать
#
# p2 = Person('Dima', 25)
# print(p2.name)


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def full_name(self):
        return (self.name + ' ' + self.surname)


    def get_older(self, years=1):
        self.age += years

    def __get_younger(self, years):  # Аналогичная фишка и с методами классов
        self.age -= years


if __name__ == "__main__":
    p = Person('Serge', 'Dmitriev', 24)
    p.get_older(3)
    print(p.full_name(), p.age)

    # p.__get_younger(5)
    # print(p.full_name(), p.age)


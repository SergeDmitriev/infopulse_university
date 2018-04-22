#     Наследование
from Lecture5.Classwork.Person import Person

# Если просто унаследоваться от класса - даже переопределенные базовые методы работают от базоваого класса
class Employee(Person):

    def __init__(self, name='', surname='', age=None, position=None, salary=0):
        # Person.__init__(self, name, surname, age)
        super().__init__(name, surname, age)
        self.position = position
        self.salary = salary

    def __str__(self):
        return  "Employee" + super().__str__()

    def income(self, month):
        return self.salary * month


if __name__ == '__main__':
    e = Employee('Sergey', 'Dmitrenko', age=22, position='QA', salary=1000)
    print('Salary is: ', e.income(5))
    print(e)

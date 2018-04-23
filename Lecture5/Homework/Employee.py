from Lecture5.Homework.Person import Person


class Employee(Person):

    def __init__(self, fullname, birth_year, position=None, experience=None, salary=0):
        super().__init__(fullname, birth_year)
        self.position = position
        self.experience = experience
        self.salary = salary

    def get_position(self):
        if self.experience < 3:
            return 'Junior ' + self.position
        elif 3 <= self.experience < 6:
            return 'Middle ' + self.position
        else:
            return 'Senior ' + self.position

    def increase_salary(self, summ):
        self.salary = self.salary + summ
        return self.salary


if __name__ == '__main__':
    e = Employee('Serge Dmitriev', 1993, 'QA', 3, 1000)
    e.increase_salary(150)
    print(e.salary)
    print(e.get_position())

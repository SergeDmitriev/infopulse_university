# 2. * Реализовать метод добавления нескольких навыков в новое свойство skills (список) новым методом add_skills.
# Тут можно выбрать разные подходы: или аргумент один и он список навыков, которым вы расширяете список-свойство skill,
#  или вы принимаете неопределённое количество аргументов и все их добавляете в список-свойство skill
from Lecture5.Homework.Employee import Employee


class ITEmployee(Employee):

    def __init__(self, *name_year, **characteristics):
        super().__init__(*name_year, **characteristics)
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

    def add_skills(self, *skills):
        for skill in skills:
            self.skills.append(skill)


if __name__ == '__main__':
    worker = ITEmployee('Sergey Dmitriev', 1993, position='QA')
    print('Skills at the beginning: ', worker.skills)
    worker.add_skill('HTML')
    print('First adding: {0}'.format(worker.skills))
    worker.add_skills('Json', 'CSS')
    worker.add_skills('c#', 'SQL', 'Python')
    print('Second adding: {0}'.format(worker.skills))
    print(vars(worker))

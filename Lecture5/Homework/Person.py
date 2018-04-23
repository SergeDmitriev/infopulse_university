import datetime


class Person(object):

    def __init__(self, full_name, birth_year):
        if len(full_name.split(sep=' ')) == 2:
            if datetime.datetime.now().year > birth_year > 1900:
                self.fullname = full_name
                self.birth_year = birth_year
            else:
                raise TypeError('Wrong birth year!')
        else:
            raise TypeError('Wrong fullname!')

    def get_name(self):
        a = self.fullname.split()
        return a[0]

    def get_surname(self):
        a = self.fullname.split()
        return a[1]

    def how_old(self, in_year=None):
        if in_year is None:
            return datetime.datetime.now().year - self.birth_year
        elif in_year > self.birth_year:
            return in_year - self.birth_year
        else:
            return '{0} cant live in {1}'.format(self.fullname, in_year)


if __name__ == '__main__':
    p = Person('Serge Dmitriev', 1993)
    print('Name is: ', p.get_name())
    print('Surname is: ', p.get_surname())
    print(p.how_old())
    print(p.how_old(in_year=1990))

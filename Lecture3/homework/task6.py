# Это уже было, но теперь оформите это функцией:
# 1)	Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True,
# если год високосный, и False иначе.
print('taskl6.1: ')


def is_year_leap(year):
    """
    :return: True, if year is leap
    """
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        print('Year is simple')
        return True
    else:
        print('Year is leap')
        return False


is_year_leap(int(input('Enter year number: ')))


# 2)	Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник
# с такими сторонами. Если треугольник существует, вернёт True, иначе False.
print('\n' + 'taskl6.2: ')


def if_triangle_exists(a, b, c):
    a = float(input('a= '))
    b = float(input('b= '))
    c = float(input('c= '))
    if (a + b) > c and (b + c) > a and (a + c) > b:
        return True
    else:
        return False


print('Can exists? ', if_triangle_exists(3,4,5))
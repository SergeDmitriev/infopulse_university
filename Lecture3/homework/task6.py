# Это уже было, но теперь оформите это функцией:
# 1)	Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True,
# если год високосный, и False иначе.
# print('taskl6.1: ')


def is_year_leap(year):
    """
    :return: True, if year is leap
    """
    try:
        if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
            return False
        elif year == 0:
            return 'Wrong year'
        else:
            return True
    except :
        return 'string values are not accepted!'



# 2)	Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник
# с такими сторонами. Если треугольник существует, вернёт True, иначе False.
# print('\n' + 'taskl6.2: ')


def if_triangle_exists(a, b, c):
    if (a + b) > c and (b + c) > a and (a + c) > b:
        return True
    else:
        return False


if __name__ == '__main__':

    # print('taskl6.1: ')
    y = input('Enter year: ')
    print('Year is leap ', is_year_leap(y))

    print('\n' + 'taskl6.2: ')
    s1 = float(input('a= '))
    s2 = float(input('b= '))
    s3 = float(input('c= '))
    print('Can exists? ', if_triangle_exists(s1, s2, s3))

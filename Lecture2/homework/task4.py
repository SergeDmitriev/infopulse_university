# Задание 4
# Даны три числа a, b, c. Определите, существует ли треугольник с такими сторонами.
# Если треугольник существует, выведите строку YES, иначе выведите строку NO.

a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))

if (a + b) > c and (b + c) > a and (a + c)> b:
    print('Yes')
else:
    print('Nope')
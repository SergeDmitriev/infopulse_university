# Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами
# и если существует, то возвращает тип треугольника Equilateral triangle (равносторонний),
# Isosceles triangle (равнобедренный), Versatile triangle (разносторонний) или не треугольник (Not a triangle).
print('\n' + 'task7: ')


def type_of_triangle(a, b, c):
    if (a + b) > c and (b + c) > a and (a + c) > b:
        if a == b == c:
            print('Equilateral triangle')
        elif a == b or a == c or b == c:
            print('Isosceles triangle')
        else :
            print('Versatile triangle')
    else:
        print('Not a triangle')


s1 = float(input('a= '))
s2 = float(input('b= '))
s3 = float(input('c= '))
type_of_triangle(s1, s2, s3)
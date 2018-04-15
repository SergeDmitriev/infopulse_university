# Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
# вычисляющую расстояние между точкой (x1, y1) и (x2, y2).
# Считайте четыре действительных числа от пользователя и выведите результат работы этой функции.
print('task9: ')

# def distance():
#     try:
#         x1 = x2 = y1 = y2 = 0
#         x1 = float(input('Enter x1:'))
#         y1 = float(input('Enter y1:'))
#         x2 = float(input('Enter x2:'))
#         y2 = float(input('Enter y2:'))
#     except (ValueError, TypeError):
#         x1 = x2 = y1 = y2 = 0
#         print('Wrong coordinates! Pls, refill')
#         distance()
#
#     from math import sqrt
#     result = sqrt((x2 - x1) ** 2 + (y2 - y1) **2 )
#     return result
#
#
# dist = distance()
# print(dist)


def distance(x1,x2, y1, y2):
    try:
        from math import sqrt
        result = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    except (ValueError, TypeError):
        print('Wrong coordinates! Pls, refill')
    return result

dis = distance(3,5,6,8)
print(dis)

# 1. Вычислите длину гипотенузы в прямоугольном треугольнике со сторонами 179 и 971.
from math import sqrt

print('\n\nTask1 result:')
a = 179
b = 971
c = round(sqrt(a ** 2 + b ** 2), 3)
print(c)


# 2. Дано двузначное число. Найдите число десятков в нем.
print('\n\nTask2 result:')

print('Enter 2 char numb:')
given_number = int(input())
v1 = given_number % 100
print(int(v1 //10))


# 3.	Дано трехзначное число. Найдите сумму его цифр.
print('\n\nTask3 result:')

print('Enter 3 char numb:')
three_char = input()
sum = 0
for i in three_char:
    sum += int(i)
print('Sum is:', sum)


# 4.	Дано целое число n. Выведите следующее за ним чётное число.
print('\n\nTask4 result:')
print('Enter int number: ')
task4 = int(input())

d = task4 % 2
if task4 % 2 == 0:
    d1 = task4 + 2
    print(d1)
else:
    d2 = task4 + 1
    print(d2)







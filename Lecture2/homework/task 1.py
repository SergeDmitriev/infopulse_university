text = input('Input text here: ')
# print(dir(text))
# 1.	Определите является ли строка записью числа. (Подсказка: ищите как это сделать с помощью методов строк)

print('\n\nTask1 result:')
if text.isdigit():
    print('Input row is a set of numbers')
else:
    print('Input row is NOT a set of numbers')

# 2.	Посчитайте сколько у вас пробелов в строке.
print('\n\nTask2 result:')

print("Space quantity: {0}".format(text.count(' ')))

# 3.	Посчитайте сколько у вас символов точки '.' в строке.
print('\n\nTask3 result:')

print("Space quantity: {0}".format(text.count('.')))

#4.	Создайте строку "Homework". Преобразуйте ее в строку длиной 100 символов, посередине которой исходное слово,
# а с обоих сторон строка заполнена пробелами. Выведите ее на экран.
print('\n\nTask4 result:')

hw = 'Homework'
tem = int(input('Enter space len: '))
hw_new = (' ' * tem + hw + ' ' * tem)
print('var1: ', '|' + hw_new + '|', '<--length of this =', len(hw_new))

hw2 = 'Homework'
print('var2: ', '|', hw2.center(98, ' '), '|')

# 5.	Сделайте первые буквы слов строки большими (upper case).
print('\n\nTask5 result:')

tas = 'qweryty asdfgh zxcvbnm'
empt_tas = ''
def str_up():
    temp_tas = tas.split(' ')
    print(temp_tas)

    a = empt_tas.join(tas)
    print('a:', a)


str_up()



# for i in range(len(tas)):
#     if tas[i] == ' ':
#         print(tas[i])



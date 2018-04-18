# Пользователь вводит строку. Разрежьте её на две равные части
# (если длина строки — чётная, а если длина строки нечётная,
# то длина первой части должна быть на один символ больше).
# Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.
print('taskl2: ')
row = input('Enter your row: ')
div = int(len(row)/2)

if len(row) == 0:
    print('Empty row!')

elif len(row) % 2 == 0:
    print('Even row')
    p1 = row[:div]
    p2 = row[div:]
    result = p2+p1
    # print('Result: ' + p1, p2, sep=',')
    print('Result: ' + result)

else:
    print('Odd row')
    p1 = row[:div+1]
    p2 = row[div+1:]
    # print('Result: ' + p1, p2, sep=',')
    result = p2+p1
    print('Result: ' + result)

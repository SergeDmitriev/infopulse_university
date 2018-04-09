# Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
# Удалите знаки препинания (пройдитесь циклом все слова и удалите методом strip знаки препинания)
# Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)
print('task 5 :')

text = """We are not, what we should be.
We are not, what we need to be.
But at least we are not, what we used to be.
(Football Coach)"""

splited_text = text.split(' ')
c = 0
n= ''
for i in range(len(splited_text)):
    n += splited_text[i].strip(',') + ' '
    if '\n' in splited_text[i]:
        c += 1
        splited_text[i] = splited_text[i].replace('\n', '_')
        # значение списка можно только переопределить, но разделить слово на два - нельзя
    c += 1
print('Word count = ', c)
print('No comma in the middle of text:' + '\n', n)

splited_text.sort()
print('\n Bad sort:', splited_text)






#
# list_to_str = str(splited_text)
# n = ''
# for j in range(len(list_to_str)):
#     n += list_to_str[j].strip(',') #.strip('[').strip(']').strip('\'')
# list(list_to_str).sort()
# print('No comma:')


# print(splited_text, sep= ';')
#


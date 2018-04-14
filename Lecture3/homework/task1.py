# Задание 1. # Пользователь вводит строку. Выловите исключения, если введённая строка слишком
# короткая.
# row = input('Enter your text here:')
# length = int(input('What length should be? :'))
text = 'Qwertyu iop asdfghjkL'

try:
    if len(text) < 15:
        text/1
except Exception:
    print('String too low!')
else:
    print(text[2],
          text[-2],
          text[:5],
          text[:-2],
          text[0::2],
          text[1::2],
          text[::-1],
          text[::-2],
          text[-2:0:-1],
          len(text), sep='\n')

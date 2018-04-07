# не учитывать пробелы
while True:
    text = input('Your text:')
    a = ' ' in text
    if (a and 'pass' in text ) or text == 'pass':
            break
    else:
        print('Not correct, try again: ')
# TODO: fix



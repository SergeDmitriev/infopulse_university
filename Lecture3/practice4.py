# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(unknown_var)
# finally:
#     print('Smth')


while True:
    a = input('Your number:')
    try:
        b = float(a)
    except (ValueError, TypeError) as e:
        print('Error:', e)
    else:
        break
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(unknown_var)
# finally:
#     print('Smth')


while True:
    a = input('Your number:')
    try:    # В блок try нужно добавлять тот код, который хотим проверить, не нужно добавлять в блок все подряд
        b = float(a)
    except (ValueError, TypeError) as e:
        print('Error:', e)
    else:
        break



def find_gip(k1, k2):
    """
    :param k1:  katet 1 length
    :param k2:  katet 2 length
    :return:
    """
    from math import sqrt
    c = sqrt(k1 ** 2 + k2 ** 2)
    return c
k1 = input('k1:')
k2 = input('k2:')
print(find_gip(4, 5))
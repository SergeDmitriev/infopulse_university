# def func(*args):
#     return args
# print(type(func()))
# # <class 'tuple'>
#
# print(func(1,2,3,4)) #(1,2,3,4)
# print(func()) # None


def sec_max(*numbers):
    l = list(numbers)
    l.sort()
    return print(l[-2])

sec_max(3, 5, 7, 9, 7, 9)
#Не работает, если элементы повторяются



def func(**kwargs):
    return str(kwargs.get('name')) +' is ' + str(kwargs.get('job'))

print(func(a = 1, b = 2))

# Задание 2
# Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов.
# Учитываем, что может быть повторяющиеся значения аргументов.


def print_second_max(*args):
    args_to_list = list(args)
    try:
        args_to_list.sort()
    except Exception as e:
        print('Sorry, data is not good. Got exception: {0}'.format(e))
        exit()
    args_to_set = set(args_to_list)
    max_value_inset = max(args_to_set)
    second_maximum = 0
    while max_value_inset in args_to_set:
        args_to_set.remove(max_value_inset)
        second_maximum = max(args_to_set)
    return second_maximum


result = print_second_max(9, 4, 2, 1, 4, 5, 6, 9, 8, 7, 0, 8, 7, 9)
print(result)

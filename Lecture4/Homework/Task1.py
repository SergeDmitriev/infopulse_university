# Задание 1. Со значениями по умолчанию
# Пишем функцию, которая генерирует песню la-la-la. Функция принимает 3 аргумента:
# 1-е число – сколько строк будет в песне. По умолчанию 3
# 2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
# 3-е число – если 0, то в конце стоит точка, если 1, то в конце стоит «!». По умолчанию 0


def generate_song(str_length=3, word_length=3, end_point=0):
    song_word = 'la'
    word_separator = '-'
    str_end_symbol = '.'

    if end_point == 1:
        str_end_symbol = '!'

    lyrics = (song_word + word_separator) * word_length
    final_song = (lyrics[:-1] + str_end_symbol + '\n') * str_length
    return final_song


# print(generate_song(str_length=5, word_length=5, end_point=1))

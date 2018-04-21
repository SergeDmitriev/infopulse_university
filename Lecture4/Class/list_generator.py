# Lecture_4 last slide
# swap keys and values in dict
dict_abc = {'a': 1, 'b': 2, 'c':3, 'd':4}
dict_123 = {v:k for k, v in dict_abc.items()}
# print(dict_123)

# tuple сгенерить нельзя
# generator expression
l = (y for y in range(1) if y%2==0)


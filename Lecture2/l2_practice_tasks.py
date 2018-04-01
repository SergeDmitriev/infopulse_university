#Найти все символы в листе (без рекурсии)
def m(p):
    _a = 0
    for i in range(len(p)):
        _b=len(p[i])
        _a=_a +_b
    return _a
	
print(m(u))

#Свап элементов (классическая задача программирования)
s = ['q', 'w', 'e']
s[0], s[-1] = s[-1], s[0]
print(s)

#Подсчитать кол-во символов в результате выполнения операции
ss = 2**179
bb = len(str(ss))
print(bb)

de = [1,  2,  3]
de.append(4)


f = {'a1': 1, 'a2': 2}
f.update({'a3': 3})
f.update({'a4': 4})
print(f)



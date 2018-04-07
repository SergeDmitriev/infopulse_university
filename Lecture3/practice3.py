# Task1 #Срезы:
s = "Hi there!"
print(s[2:8:-1]) #пустота
print(s[8:2:-1] + '\n')

# Task2 method args print()
a = 'text'
b = 1
print(a, b, sep=',', end='')
print(a,b, sep='\n')
print(a, b , '\n',  sep='')


# Task3
f = [1]
h = None
y = f.append(1)
print(f, h, y, sep='\n')


# Task4
l = [1, 10, 3, 6, 7, 11]
even = []
odd = []

for item in l: #не len(), поскольку python сам определит длинну списка
    if item % 2 == 0:
        even.append(item)
    elif item % 2 ==1:
        odd.append(item)
    else:
        print(item, 'is not integer')
print(even)
print(odd)

# Task4
owner_users = {'username': 'case6', 'password': 'Qq123456'}
for key in owner_users:
    print(key, owner_users[key])
# Есть стандартные методы: dict.values() dict.keys, dict.items() --возвращает пару
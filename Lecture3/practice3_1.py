l = [1, 10, 3, 6, 7, 11]

for num in l:
    if num % 2 ==0:
        print(num)
    elif num % 2 != 0:
        num+=1
        print('odd', num)
    else:
        print('Type error')


lis = [1, 10, 3, 6, 7, 11]
print('Before', lis)

# Замена элемента
for i in range(len(lis)):
    if lis[i] % 2 != 0:
        lis[i] += 1

print('After', lis)



# Для цикла list не нужен
for i in range(10):
    print(i)

print(list(range(2, 7, 2)))





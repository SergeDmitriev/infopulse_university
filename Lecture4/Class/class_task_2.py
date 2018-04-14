# sample2

while True:
    a = input('Input less than 10 symbols:')
    if len(a) <10: break
    assert len(a) < 10
    print(a)


# mass = -100
# assert mass >100, 'message'


def check(list1, list2, list3):
    assert type(list1) is type(list1) is type(list3) is list
    joint_list = list1 + list2 + list3
    return  max(joint_list)

a = [1,2,3]
b = [4,5,6]
c = 789
res = check(a,b,c)
print(res)







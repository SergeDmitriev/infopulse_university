from Lecture4.Homework.Task1 import generate_song

# write to file
res = open('D:\Work\Infopulse\infopulse_university\Lecture6\Class\lalalal.txt', 'w')
res.write(generate_song(str_length=5, word_length=5, end_point=1))
res.close()

# read program code
pers = open('D:\Work\Infopulse\infopulse_university\Lecture5\Homework\Person.py', 'r')
print(pers.read())
pers.read()

# read file in cycle
lin_reading_file = open('D:\Work\Infopulse\infopulse_university\Lecture4\Homework\Task1.py', 'r', encoding='utf-8')
for i in lin_reading_file:
    print(i.rstrip() + '!')
lin_reading_file.close()


if __name__ == '__main__':
    pass

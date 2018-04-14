
def enter():
    while True:
        text = input('Enter your text:')
        try:
            assert text.isalpha()
        except:
            text
            enter()
        return text

a = enter()
print(a)
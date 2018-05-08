with open('text_files/task3.Base_file.txt', 'r', encoding='utf8') as read_file:
    with open('text_files/task3.text_in_alphab_order.txt', 'w', encoding='utf8') as write_file:
        list_of_words = []
        for line in read_file:
            list_of_words += line.split()
        list_of_words.sort()
        for word in list_of_words:
            quantity = list_of_words.count(word)
        # b = (' '.join(str(e) for e in a) + '\n')
            write_file.write(str(quantity) + ' ' + str(word) + '\n')

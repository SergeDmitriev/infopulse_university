#original file list1.py

# # Google's Python Class
# # http://code.google.com/edu/languages/google-python-class/
#
# # Basic list exercises
# # Fill in the code for the functions below. main() is already set up
# # to call the functions with a few different inputs,
# # printing 'OK' when each function is correct.
# # The starter code for each function includes a 'return'
# # which is just a placeholder for your code.
# # It's ok if you do not complete all the functions, and there
# # are some additional functions to try in list2.py.
#
# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.


def match_ends(list_of_strings):
    counter = 0
    for i in range(len(list_of_strings)):
        if len(list_of_strings[i]) >= 2 and list_of_strings[i][0] == list_of_strings[i][-1]:
            counter +=1
    return counter


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.

def front_x(words):
    list_with_first_x = []
    list_of_others_elements = []
    for i in range(len(words)):
        if words[i][0] == 'x':
            list_with_first_x.append(words[i])
        else:
            list_of_others_elements.append(words[i])
    list_with_first_x.sort()
    list_of_others_elements.sort()
    return list_with_first_x + list_of_others_elements


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use sorted() function and a custom key= function to extract the last element form each tuple.

# using 2 functions:
# def sort_last(tuples):
#     def extract_the_last_element(tup):
#         return tup[-1]
#     return sorted(tuples, key=extract_the_last_element)

#using lambda:
def sort_last(tuples):
    return sorted(tuples, key=lambda x: x[-1])

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{0} got: {1} expected: {2}'.format(prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print('\n', 'front_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print('\n', 'sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    # test(sort_last([(2, 3), (1, 2), (3, 1)]),
    #      [(3, 1), (1, 2), (2, 3)])
    # test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
    #      [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()

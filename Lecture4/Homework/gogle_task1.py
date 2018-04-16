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

def match_ends(*list_of_strings):
    symbol_counter = 0
    for i in range(len(list_of_strings)):
        element = list_of_strings[i]
        if len(element) >= 2 and element[0] == element[-1]:
            symbol_counter +=1
    return symbol_counter

print('Result of task1: ', match_ends('vc', 'gg', 'a1z', 'b2x', 'c3c', 'd4v', 'zxcvz', 'xcccx', 'z', 'xc', 'f', 'g', 'L', 'd', '4564'))


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.

def front_x(*words):
    input_list = list(words)
    list_with_first_x = []
    for i in range(len(input_list)):
        element = input_list[i]
        if element[0] == 'x':
            list_with_first_x.append(input_list[i])
            # print(input_list[i])
        # else




    return p

print('Result of task2: ', front_x('vc', 'xgg', 'a1z', 'xb2x', 'c3c', 'd4v', 'zxcvz', 'xcccx', 'z', 'xc', 'f', 'g', 'L', 'xd', '4564'))


#
# # C. sort_last
# # Given a list of non-empty tuples, return a list sorted in increasing
# # order by the last element in each tuple.
# # e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# # [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# # Hint: use sorted() function and a custom key= function to extract the last element form each tuple.
# def sort_last(tuples):
#     # +++your code here+++
#     return
#
#
# # Simple provided test() function used in main() to print
# # what each function returns vs. what it's supposed to return.
# def test(got, expected):
#     if got == expected:
#         prefix = ' OK '
#     else:
#         prefix = '  X '
#     print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))
#
#
# # Calls the above functions with interesting inputs.
# def main():
#     print('match_ends')
#     test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
#     test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
#     test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)
#
#     print('\n', 'front_x')
#     test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
#          ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
#     test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
#          ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
#     test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
#          ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
#
#     print('\n', 'sort_last')
#     test(sort_last([(1, 3), (3, 2), (2, 1)]),
#          [(2, 1), (3, 2), (1, 3)])
#     test(sort_last([(2, 3), (1, 2), (3, 1)]),
#          [(3, 1), (1, 2), (2, 3)])
#     test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
#          [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
#
#
# if __name__ == '__main__':
#     main()

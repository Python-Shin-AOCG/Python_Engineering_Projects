'''
Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
how are you you are my angel baby I love you love you forever
Then, the output should be:
I angel are baby forever how love my you
'''

def wordSort():
    s = set(input().split(' '))
    lst = []
    for word in s:
        word = word.lower()
        lst.append(word)
    lst = sorted(lst)
    print(' '.join(lst))

wordSort()


'''
Question:
Write a program that accepts a comma separated sequence of words as input and prints the words and numbers in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
Korea, Germany, America, 30, 10, 20
Then, the output should be:
10,20,30
America,Germany,Korea

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

def inputSort():
    numList = []
    wordList = []
    userInput = input("Enter your input: ").split(',')
    for i in userInput:
        if i.isdigit():
            numList.append(i)
        else:
            wordList.append(i)

    print(sorted(numList))
    print(sorted(wordList))

inputSort()


'''
Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
1010, 1001, 100011, 1111, 1100, 111
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input
'''

def decimal():
    result = []
    repo = input("Enter your binary numbers: ").split(',')
    for num in repo:
        decimal = int(num,2)
        if decimal %5 == 0:
            result.append(str(num))
    print(','.join(result))

decimal()

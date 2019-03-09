'''
Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
10
Then, the output should be:
3628800
'''

#20! = 20 * 19 * 18 * 17 * ..* 1
#21! = 21 * 20 * 19 * 18 ... * 1

#x! = x * x-1 * x-2 ... * 1
#x! = x * factorial(x-1)
#x-1 ! = x-1 * facotorial(x-2)


def factorial(number):
    #0! = 1
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)


userInput = int(input("Enter a number that you want to calculate: "))
print(factorial(userInput))

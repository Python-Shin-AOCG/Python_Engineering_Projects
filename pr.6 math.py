'''

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 60. H is 10.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,200,300
The output of the program should be:
11,15,19

Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0,
it should be printed as 26)
In case of input data being supplied to the question, it should be assumed to be a console input. 

'''

from math import *        
def formula():
    C = 60
    H = 10
    consoleInput = input("Enter your integers: ").split(',')
    lst = []
    print(consoleInput)
    for D in consoleInput:
        Q = round(sqrt(2*C*int(D)/H))
        lst.append(str(Q))
    print(','.join(lst))

formula()

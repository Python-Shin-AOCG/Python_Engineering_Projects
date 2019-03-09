'''
Question:
Define a class which has at least five methods:
getInteger: to get two integers from console input
printIntegers: to print integers.
addInteger: to add two integers together
subtractInteger: to subtract two integers
powerInteger: to get the power of the first integer to the power of second intger
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
'''

from math import pow

class InputIntegerOut():
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def getInteger(self):
        self.num1 = int(input("Enter your first integer: "))
        self.num2 = int(input("Enter your second integer: "))

    def printInteger(self):
        print("First integer is", self.num1)
        print("Second integer is", self.num2)

    def addInteger(self):
        print("The sum of these two integers is", self.num1 + self.num2)

    def subtractInteger(self):
        print("The difference between these two integers is", abs(self.num1-self.num2))

    def powerInteger(self):
        print("The result of the first integer to the power of the second integer is", pow(self.num1,self.num2))

intSample = InputIntegerOut()
intSample.getInteger()
intSample.printInteger()
intSample.addInteger()
intSample.subtractInteger()
intSample.powerInteger()


        

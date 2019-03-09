'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

def caseSensitive():
    outputDict = {"UPPER CASE":0, "LOWER CASE":0}
    userInput = input("Enter your sentence: ")
    for c in userInput:
        if c.islower():
            outputDict["LOWER CASE"] += 1
        elif c.isupper():
            outputDict["UPPER CASE"] += 1

    print("UPPER CASE ", outputDict["UPPER CASE"])
    print("LOWER CASE ", outputDict["LOWER CASE"])

caseSensitive()

            
        

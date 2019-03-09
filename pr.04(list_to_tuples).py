'''
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
10,20,30,40,50,60
Then, the output should be:
['10', '20', '30', '40', '50', '60']
('10', '20', '30', '40', '50', '60')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple
'''

def listOrtuple():
    listMaterial = input("Enter your integers: ").split(',')
    tupleMaterial = tuple(listMaterial)
    print("list Material is", listMaterial)
    print("tuple Material is", tupleMaterial)

listOrtuple()



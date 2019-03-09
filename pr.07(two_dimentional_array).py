'''
Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,6
Then, the output of the program should be:
[[0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5], [0, 2, 4, 6, 8, 10]]

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

'''

def two_dim_array():
    x = int(input("Enter your preferrable row value: "))
    y = int(input("Enter your preferrable column value: "))

    final = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(i*j)
        
        final.append(row)
    return final

print(two_dim_array())

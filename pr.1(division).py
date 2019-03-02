'''
Question:
Write a program which will find all such numbers which are divisible by 3 but are not a multiple of 5,
between 1000 and 5000 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

def numbers():
    lst = []
    for i in range(1000,5001):
        if i%3 == 0 and i%5 != 0:
            lst.append(str(i))
    print(','.join(lst))

numbers()
    


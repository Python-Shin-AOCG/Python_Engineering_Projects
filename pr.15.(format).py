'''
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

'''

def format():
    a = input("Enter your digit: ")
    #9+99+999+9999
    aa = int(a+a)
    aaa = int(str(aa)+a)
    aaaa = int(str(aaa)+a)
    print(int(a)+aa+aaa+aaaa)

print(format())
    

'''
Given an array, rotate the array to the right by k steps, k is non-negative.
Try to optimize the time complexity.

input: [1,2,3,4,5], k=2
output: [4,5,1,2,3]

input: [0,1,2,3,4], k=1
output: [4,0,1,2,3]
'''

def rotation(k):
    arr = [int(x) for x in input().split(',')]
    result = [0] * len(arr)
    for i in range(len(arr)):
        if i+k < len(arr):
            result[i+k] = arr[i]
        else:
            new_index = (i+k) % len(arr)
            result[new_index] = arr[i]
    return result

k = int(input())
print(rotation(k))
        

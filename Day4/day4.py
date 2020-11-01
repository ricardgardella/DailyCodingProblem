'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

I know this solutions is O(logN) instead of N. But this is the approach that I'd take in a interview of approx 30 minutes. If you want to go O(N) you'd need to go with Hash.
'''
import numpy as np
def find_missing_positive(A):
    A = np.array(A)
    A = A[A>=0]
    A = np.sort(A)
    if len(A) == 0:
        return None
    for i in range (0,len(A)):
        if i == len(A)-1:
            return A[i]+1
        if A[i] - A[i+1] == -2:
            return A[i]+1
A = [1, 2, 0]
print(find_missing_positive(A))
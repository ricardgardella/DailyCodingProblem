'''
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

import numpy as np
A = [10, 15, 3, 7,100,20]
K = 17

def add_up(A,K): #Binary search to have log(N)
    A = np.sort(A)
    low = 0
    high = len(A)-1
    while low <= high:
        if A[low] + A[high] == K:
            return True
        elif A[low] + A[high] > K:
            high -= 1
        elif A[low] + A[high] < K:
            low += 1
    return False
print(add_up(A,K))


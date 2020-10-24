"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Approach: two pointers
"""

def sortedSquares(nums):
    n = len(nums)
    result = [0] * len(nums)
    left, right = 0, n-1
    highestIndex = right
    while left <= right:
        leftsq = nums[left] ** 2
        rightsq = nums[right] **2

        if leftsq > rightsq:
            result[highestIndex] = leftsq
            left += 1
        else:
            result[highestIndex] = rightsq
            right -= 1
        highestIndex -= 1

    print(result)

sortedSquares([-4,-1,0,3,10])

sortedSquares([-7,-3,2,3,11])



""" using collections and two pointer
from collections import deque

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        result = deque()
        left, right = 0, n-1
        while left <= right:
            l = abs(A[left])
            r = abs(A[right])
            if l < r:
                result.appendleft(r ** 2)
                right -= 1
            else:
                result.appendleft(l ** 2)
                left += 1
            
        return list(result)
"""
    
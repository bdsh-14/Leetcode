''' 
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3]


educative.io
'''

def max_sum(k, nums):
    windowStart = 0
    windowSum = 0
    max_sum = 0

    for windowEnd in range(len(nums)):
        windowSum += nums[windowEnd]
        if windowEnd >= k-1:
            max_sum = max(max_sum, windowSum)
            windowSum -= nums[windowStart]
            windowStart += 1
    return max_sum


a = max_sum(3, [2, 1, 5, 1, 3, 2])
print(a)

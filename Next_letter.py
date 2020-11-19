"""
Input: ['a', 'c', 'f', 'h'], key = 'f'
Output: 'h'
Explanation: The smallest letter greater than 'f' is 'h' in the given array.
"""


def next_letter(nums, key):
    n = len(nums)
    if key > nums[n-1] or key < nums[0]:
        return nums[0]

    start = 0
    end = n-1
    while start <= end:
        mid = start + (end-start)//2
        if key >= nums[mid]:
            start = mid + 1
        else:
            end = mid - 1
        
    return nums[start % n]

print(next_letter(['a', 'c', 'f', 'h'], 'f'))
print(next_letter(['a', 'c', 'f', 'h'], 'b'))
print(next_letter(['a', 'c', 'f', 'h'], 'm'))


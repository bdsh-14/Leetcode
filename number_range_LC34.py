"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
"""

def find_range(nums, key):
    result = [-1, -1]
    result[0] = binarySearch(nums, key, False)
    if result[0] != -1 :
        result[1] = binarySearch(nums,key, True)
    return result

def binarySearch(nums, key, targetFound):
    end = len(nums) - 1
    keyIndex = -1
    start = 0
    while start <= end:
        mid = start + (end - start) // 2
        if key > nums[mid]:
            start = mid + 1
        elif key < nums[mid]: 
            end = mid -1 
        else:
            keyIndex = mid
            if targetFound:
                start = mid + 1
            else:
                end = mid - 1
    return keyIndex

            

print(find_range([4, 6, 6, 6, 9], 6))
print(find_range([1, 3, 8, 10, 15], 10))
print(find_range([1, 3, 8, 10, 15], 12))
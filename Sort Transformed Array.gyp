"""


Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]

Approach: 2 pointers, parabola

Refer to: https://leetcode.com/problems/sort-transformed-array/discuss/766072/Python-3-with-detailed-explanation-with-ascii-drawing
for more explanation

""" 

def sortTransformedArray(nums, a, b, c):
    result = [0] * len(nums)
    nums = [a*i**2 + b*i + c for i in nums]
    left, right = 0, len(nums) - 1
    index = 0 if a<0 else right
    while left <= right:
        if a>=0:
            if nums[left] > nums[right]:
                result[index]= nums[left]
                left+=1
            else:
                result[index] = nums[right]
                right -= 1
            index -= 1
        else:
            if nums[left] > nums[right]:
                result[index] = nums[right]
                right -= 1
            else:
                result[index] = nums[left]
                left += 1
            index += 1
    
    print(result)
    
        

#sortTransformedArray([-4,-2,2,4], 1, 3, 5)

# nums = [-4,-2,2,4], a = -1, b = 3, c = 5

sortTransformedArray([-4,-2,2,4], -1, 3, 5)
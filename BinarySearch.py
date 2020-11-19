def binary_search(nums, target):
    nums = sorted(nums)
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = start + (end - start)//2

        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1


print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
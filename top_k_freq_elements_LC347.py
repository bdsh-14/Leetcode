# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

from heapq import *

def topKFrequent(nums, k):
    topelements = []
    dic = {}
    minheap = []

    for num in nums:
        dic[num] = dic.get(num, 0) + 1

    #print(dic)
    
    for n,f in dic.items():
        heappush(minheap, (f, n))
       # print("After pushing: ", minheap)
        if len(minheap) > k:
            heappop(minheap)
            #print("After popping: ", minheap)
        
        
    while minheap:
        topelements.append(heappop(minheap)[1])

    return topelements


nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
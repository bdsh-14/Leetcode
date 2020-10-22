"""
3. Longest Substring Without Repeating Characters

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Approach: Sliding window
"""

def lengthOfLongestSubstring(s):
    substring = []
    maxLength = 0

    for i in s:
        if i in substring:
            substring = substring[substring.index(i)+1:]
        substring.append(i)
        maxLength = max(maxLength, len(substring))

    return maxLength


s = "abcabcbb"
maxlen1 = lengthOfLongestSubstring(s)
print(maxlen1)

t = "pwwkew"
maxlen2 = lengthOfLongestSubstring(t)
print(maxlen2)

u = "bbbbb"
maxLen3 = lengthOfLongestSubstring(u)
print(maxLen3)







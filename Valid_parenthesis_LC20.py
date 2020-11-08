"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Approach: using a stack and dictionary
"""

def isValid(s):
    mapping = { ")": "(", "}": "{", "]":"[" }
    stack = []
    for i in s:
        if stack:
            if i in mapping.keys():
                top = stack.pop()
                if top != mapping[i]:
                    return False
            else:
                stack += i
        else: 
            stack += i
    print(not stack)

isValid("()")


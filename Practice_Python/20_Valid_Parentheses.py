'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''
class Solution:
    def isValid(self, s: str) -> bool:
        
        dictf = {
             ")": "(",
             "}": "{", 
             "]": "["
        }
        
        temp = ["q"]
        for ele in s:
            if ele in dictf:
                if temp[-1] == dictf[ele]:
                    temp.pop()
                else:
                    temp.append(ele)            
            else:
                temp.append(ele) 
        if len(temp)==1:
            return True
        else:
            return False

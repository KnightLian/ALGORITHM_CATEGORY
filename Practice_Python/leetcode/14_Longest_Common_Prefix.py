'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)>0:
            def recur(strs):
                # print(strs)
                if len(strs) ==1:
                    return strs[0]
                else:                
                    strlen = min(len(strs[0]),len(strs[1]))
                    temp = ''
                    for i in range(strlen):
                        if strs[0][0] == strs[1][0]:
                            if strs[0][i] == strs[1][i]:
                                temp += strs[0][i]
                    del strs[0]
                    del strs[0]
                    strs.insert(0,temp)
                    return recur(strs)          

            return recur(strs)
        else:
            return ''
        

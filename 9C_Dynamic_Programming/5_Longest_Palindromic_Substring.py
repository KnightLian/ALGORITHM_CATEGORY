'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size == 0 or size ==1:
            return s
        dp = [[False]*size for _ in range(size)]
        # print(dp)

        max_len = 1
        start = 0
        
        for i in range(size):
            dp[i][i] = True
        # print(dp)

        for j in range(1,size):
            for i in range(0,j):
                if s[i] == s[j]:
                    if j - 1 - (i + 1) + 1 < 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]    
                else:
                    dp[i][j] = False
                
                if dp[i][j] == True:
                    cur_len = j-i+1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
                    
        return s[start: (start + max_len)]
        # print(dp)

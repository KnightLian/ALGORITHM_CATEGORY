'''
Given a string s, 
partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example:
Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Help Video: https://m.youtube.com/watch?v=WPr1jDh3bUQ
'''

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        for j in range(1,n):
            for i in range(0,j):
                if s[i] == s[j]:
                    if (j-1) - (i+1) +1 <2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
        # print(dp)

        cutf = [0] * n
        # print(cutf)
        for i in range(n):
            temp = float('inf')
            if dp[0][i] == True:
                cutf[i] = 0
            else:
                for j in range(i):
                    if dp[j+1][i] == True and temp > cutf[j]+1:
                        temp = cutf[j]+1
                cutf[i] = temp
       # print(cutf)                
        return cutf[-1]
 

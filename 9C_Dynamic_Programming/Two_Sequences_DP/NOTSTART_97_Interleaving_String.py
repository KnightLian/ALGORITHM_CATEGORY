'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
'''

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1+n2 != len(s3):
            return False

        dp = [[False]*(n2+1) for _ in range(n1+1)]       
        dp[0][0] = True

        for i in range(1, n2+1):
            if s2[:(i-1+1)] == s3[:(i-1+1)]: # include the ith letter
                dp[0][i] = True
        for i in range(1, n1+1):
            if s1[:(i-1+1)] == s3[:(i-1+1)]: # include the ith letter
                dp[i][0] = True
        # print(dp)
        
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if s1[i-1] == s3[i+j-1] and dp[i-1][j] == True:
                    dp[i][j] = True
                elif s2[j-1] == s3[i+j-1] and dp[i][j-1] == True:
                    dp[i][j] = True

        return dp[-1][-1]
      

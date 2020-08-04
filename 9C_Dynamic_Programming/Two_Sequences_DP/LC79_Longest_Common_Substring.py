'''
Given two strings, find the longest common substring.
Return the length of it.

Example 1:
	Input:  "ABCD" and "CBCE"
	Output:  2
	Explanation:
	Longest common substring is "BC"


Example 2:
	Input: "ABCD" and "EACB"
	Output:  1
	Explanation: 
	Longest common substring is 'A' or 'C' or 'B'
'''

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        n1 = len(A)
        n2 = len(B)
        
        dp = [[0]*(n2+1) for _ in range(n1+1)]
    
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = 0
        temp = 0
        for row in dp:
            temp = max(temp, max(row))
        # print(dp)
        return temp

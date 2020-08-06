'''
Given a string S and a string T, 
count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string 
which is formed from the original string by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters. 
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It's guaranteed the answer fits on a 32-bit signed integer.

Example 1:
Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)
rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

Example 2:
Input: S = "babgbag", T = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)
babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^

Hint:
dp[i][j]表示S[0~i]包含的T[0~j]的个数。当S[i]==T[j]时，dp[i][j]=dp[i-1][j]+dp[i-1][j-1]。
dp[i-1][j]表示S[0~i-1]包含的T[0~j]的个数，dp[i-1][j-1]表示S[0~i-1]包含的T[0~j-1]的个数。
前者的意思是，不管S[i]是什么，至少知道S[0~i-1]包含的T[0~j]的个数。
后者的意思是，当加入S[i]和T[j]，且S[i]==T[j]时，这时候S[0~i]就刚好包含T[0~j]，
包含的个数，取决于S[0~i-1]包含多少个T[0~j-1]。

S[j] !== T[i]，
此时对于子序列的出现个数没有影响，等于T的前i位在S的前j - 1位的子序列个数。

S[j] === T[i]，
例如S = 'baba', T = 'ba'，两者最后一位相等，
ba在baba的子序列中出现的个数等于下面两个情况相加:
1) ba在bab的中出现的个数为1，即遍历至T的j-1位时的出现个数。
2) b在bab的中出现的个数为2，S[j]与T[i]相等，ba在baba中所增加的出现个数也为2。

在S和T前面随意加一个字符，当i==0或j==0时，表示空串。
试想如果T为空，无论S为什么，都包含一个T，即包含一个空串。所以要初始化dp[0~S1.length][0]=1。
'''

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ns = len(s)
        nt = len(t)

        dp = [[0]*(ns+1) for _ in range(nt+1)]
        
        for i in range(ns+1):
            dp[0][i] = 1

        for i in range(1, nt+1):
            for j in range(1, ns+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

        return dp[-1][-1]

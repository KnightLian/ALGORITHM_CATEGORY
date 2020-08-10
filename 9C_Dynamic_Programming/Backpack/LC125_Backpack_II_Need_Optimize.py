'''
0/1 Knapsack Problem

There are n items and a backpack with size m. 
Given array A representing the size of each item and array V representing the value of each item.
What's the maximum value can you put into the backpack?

-A[i], V[i], n, m are all integers.
-You can not split an item.
-The sum size of the items you want to put into backpack can not exceed m.
-Each item can only be picked up once

Example 1:
Input: m = 10, A = [2, 3, 5, 7], V = [1, 5, 2, 4]
Output: 9
Explanation: Put A[1] and A[3] into backpack, getting the maximum value V[1] + V[3] = 9 

Example 2:
Input: m = 10, A = [2, 3, 8], V = [2, 5, 8]
Output: 10
Explanation: Put A[0] and A[2] into backpack, getting the maximum value V[0] + V[2] = 10 

O(nm) memory is acceptable, can you do it in O(m) memory?

Help: https://www.youtube.com/watch?v=xCbYmUPvc2Q&t=773s
'''

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here

        n = len(A)
        dp = [[0]*(m+1) for _ in range(n)]
        
        # initialize for 1st iterm
        for i in range(m+1):
            if i >= A[0]:
                dp[0][i] = V[0]
                
        for i in range(1, n):
            for j in range(1, m+1):
                # if weight constrain is bigger 
                # consider to choose iterm i or not
                if j >= A[i]: 
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i]]+V[i])
                    
                # otherwise    
                # have to not choose iterm i    
                else: 
                    dp[i][j] = dp[i-1][j] 
                
    #     print(dp)        
        return dp[-1][-1]
    

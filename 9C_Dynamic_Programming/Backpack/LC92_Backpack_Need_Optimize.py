'''
Given n items with size Ai, 
an integer m denotes the size of a backpack. How full you can fill this backpack?

-You can not divide any item into small pieces.

Example 1:
	Input:  [3,4,8,5], backpack size=10
	Output:  9

Example 2:
	Input:  [2,3,5,7], backpack size=12
	Output:  12
  
O(n x m) time and O(m) memory.
O(n x m) memory is also acceptable if you do not know how to optimize memory.
'''

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        dp = [[0]*(m+1) for _ in range(n)]
        
        #initialize 1st weight
        for i in range(m+1):
            if i >= A[0]:
                dp[0][i] = A[0]
        
        for i in range(1, n):
            for j in range(1, m+1):
                # if weight constrain is bigger 
                # consider to choose iterm i or not                
                if j >= A[i]:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-A[i]]+A[i])
                # otherwise    
                # have to not choose iterm i                       
                else:
                    dp[i][j] = dp[i-1][j]
                    
        #print(dp)
        return dp[-1][-1]

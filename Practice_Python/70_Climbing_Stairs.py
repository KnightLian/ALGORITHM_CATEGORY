'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        #Dynamic Programming Fibonacci Number
        if n == 1:
            return 1
        elif n ==2:
            return 2
        elif n ==0:
            return 0
        
        list0 = [0]*n
        list0[0] = 1
        list0[1] = 2
        
        for i in range(2,n):
            list0[i]=list0[i-1]+list0[i-2]
        return list0[n-1]
        

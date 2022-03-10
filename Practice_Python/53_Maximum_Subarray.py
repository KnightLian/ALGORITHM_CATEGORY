'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

class Solution:         
    def maxSubArray(self, nums: List[int]) -> int:        
        #Kadane's
        locmax = nums[0]
        glomax = nums[0]       
        for i in range(1,len(nums)):
            locmax = max((locmax + nums[i]),nums[i])
            if locmax > glomax:
                glomax = locmax
        return glomax
          

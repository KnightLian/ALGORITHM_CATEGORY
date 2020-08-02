'''
Given a triangle, find the minimum path sum from top to bottom. 
Each step you may move to adjacent numbers on the row below.
For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, 
where n is the total number of rows in the triangle.
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # print(triangle)
        for row in range(1,len(triangle)):
            for col in range(len(triangle[row])):
                if col == 0 :
                    triangle[row][col] = triangle[row][col] + triangle[row-1][col] 
                elif col == len(triangle[row])-1:
                    triangle[row][col] = triangle[row][col] + triangle[row-1][-1] 
                else:
                    triangle[row][col] = triangle[row][col] + \
                    min(triangle[row-1][col-1],triangle[row-1][col])
        return min(triangle[-1])

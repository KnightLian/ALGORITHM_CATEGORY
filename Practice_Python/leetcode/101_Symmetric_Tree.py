'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:       
        if root == None:
            return True
        return self.isMirror(root.left, root.right)     
    def isMirror(self, a, b):
        if a == None and b == None:
            return True     
        if a == None or b == None:
            return False
        return a.val == b.val and self.isMirror(a.right, b.left) \
                and self.isMirror(a.left, b.right)
     

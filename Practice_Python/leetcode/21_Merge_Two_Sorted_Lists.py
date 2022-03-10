'''
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:               
        goal = ListNode(float('-inf'))
        pointer = goal  
        
        if l1 is None:
            return l2        
        if l2 is None:
            return l1         
        if l1 is None and l2 is None:
            return l1     
            
        while  True:          
            if l1.val < l2.val:
                pointer.next = l1
                l1 = l1.next
            else:
                pointer.next = l2
                l2 = l2.next
            pointer = pointer.next
            if l1 is None:
                pointer.next = l2
                break
            if l2 is None:
                pointer.next = l1
                break       
        return goal.next  

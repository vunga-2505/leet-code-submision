# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next
        c = head
        while c and c.next:
            if c.next.val == val:
                c.next = c.next.next
            else:
                c= c.next
    
        return head
        
# @lc code=end
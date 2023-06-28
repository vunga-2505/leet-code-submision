# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        p = None
        current = head
    
        while current:
            next = current.next
            current.next = p
            p = current
            current = next
    
        return p
# @lc code=end


# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result = []
        if root is not None:
            result += self.inorderTraversal(root.left)
            result.append(root.val)
            result += self.inorderTraversal(root.right)
        return result
# @lc code=end

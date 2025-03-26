# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root):
        
        def DFS(l, r, level):
            if not l or not r:
                return
            if level % 2 == 0:
                l.val, r.val = r.val, l.val
            DFS(l.left, r.right, level + 1)
            DFS(l.right, r.left, level + 1)
        DFS(root.left, root.right, 0)
        return root
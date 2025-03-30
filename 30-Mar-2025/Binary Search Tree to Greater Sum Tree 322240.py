# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root):
        node_sum = [0]
        self.bst_to_gst_helper(root, node_sum)
        return root
    def bst_to_gst_helper(self, root, node_sum):
        if root is None:
            return
        self.bst_to_gst_helper(root.right, node_sum)
        node_sum[0] += root.val
        root.val = node_sum[0]
        self.bst_to_gst_helper(root.left, node_sum)
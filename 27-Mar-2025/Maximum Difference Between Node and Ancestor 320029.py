# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def preord(root, mini, maxi):
            if not root:
                return maxi - mini
            mini = min(mini, root.val)
            maxi = max(maxi, root.val)

            l = preord(root.left, mini, maxi)
            r = preord(root.right, mini, maxi)
            return max(l, r)
        return preord(root, root.val, root.val)
        
# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def madpths(root, d):
            if not root: 
                return d
            return max(madpths(root.left, d + 1), madpths(root.right, d + 1))        
        return madpths(root, 0)
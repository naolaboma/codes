# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def find(node):
            if not node:
                return 0
            left=1+find(node.left)
            right = 1+find(node.right)
            return max(left,right)
        return find(root)
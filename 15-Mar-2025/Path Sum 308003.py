# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack = []
        def preord(root, targetSum):
            if not root:
                return False
            stack.append(root.val)
            if not root.left and not root.right:
                if sum(stack) == targetSum:
                    return True
                    
            lef = preord(root.left, targetSum)
            rig = preord(root.right, targetSum)
            stack.pop()
            return lef or rig
        return preord(root, targetSum)
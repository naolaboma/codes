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
            left_result = preord(root.left, targetSum)
            right_result = preord(root.right, targetSum)
            stack.pop()
            return left_result or right_result
        return preord(root, targetSum)
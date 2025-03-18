# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(node, level):
            if not node:
                return
            if level == len(result):
                result.append(node.val)
            else:
                result[level] = max(result[level], node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        result = []
        dfs(root, 0)
        return result
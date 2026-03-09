# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        ii = {inorder[i]: i for i in range(len(inorder))}
        pi = len(postorder) - 1

        def build(l, r):
            nonlocal pi
            if l > r:
                return None
            
            rv = postorder[pi]
            pi -= 1
            root = TreeNode(rv)

            m = ii[rv]

            root.right = build(m + 1, r)
            root.left = build(l, m - 1)

            return root

        return build(0, len(inorder) - 1)
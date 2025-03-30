# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.matchingSubtreeCount = 0
    def calculateSubtreeValues(self, currentNode):
        if currentNode is None:
            return 0, 0
        leftSubtree  = self.calculateSubtreeValues(currentNode.left)
        rightSubtree = self.calculateSubtreeValues(currentNode.right)
        sumOfValues  = leftSubtree [0] + rightSubtree[0] + currentNode.val
        numberOfNodes  = leftSubtree [1] + rightSubtree[1] + 1
        if sumOfValues  // numberOfNodes  == currentNode.val:
            self.matchingSubtreeCount += 1
        return sumOfValues , numberOfNodes
    def averageOfSubtree(self, root):
        self.calculateSubtreeValues(root)
        return self.matchingSubtreeCount 
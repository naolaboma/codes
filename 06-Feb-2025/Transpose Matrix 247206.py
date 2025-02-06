# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix[0])
        column = len(matrix)
        ans = []
        for i in range(rows):
            ans.append([0]*column)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                ans[j][i] = matrix[i][j]
        return ans
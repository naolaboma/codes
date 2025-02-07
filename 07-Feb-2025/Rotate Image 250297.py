# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        transp = [[0]*n for j in range(n)]
        for i in range(n):
            for j in range(n):
                transp[j][n-i-1] = matrix[i][j]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = transp[i][j]
        
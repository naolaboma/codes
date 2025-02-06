# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def needed(a):
            n= len(a)
            c = [[0]*n for i in range(n)]
            for i in range(n):
                for j in range(n):
                    c[j][n -i -1] = mat[i][j]
            return c
        for i in range(4):
            if mat == target:
                return True
            else:
                mat = needed(mat)
        return False
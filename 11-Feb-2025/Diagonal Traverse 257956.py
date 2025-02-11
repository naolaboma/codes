# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        diagonals = {}
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                key = i + j
                if key not in diagonals:
                    diagonals[key] = []
                diagonals[key].append(mat[i][j])
        result = []
        for key in sorted(diagonals.keys()):
            if key % 2 == 0:
                result.extend(diagonals[key][::-1])
            else:
                result.extend(diagonals[key])
        return result
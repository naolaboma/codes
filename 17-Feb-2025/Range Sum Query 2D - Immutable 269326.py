# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, col = len(matrix), len(matrix[0])
        self.presm = [[0] * (col + 1) for _ in range(rows + 1)]
        for i in range(1, rows + 1):  
            for j in range(1, col + 1):  
                self.presm[i][j] = (
                    self.presm[i][j - 1] +  
                    self.presm[i - 1][j] -  
                    self.presm[i - 1][j - 1] +  
                    matrix[i - 1][j - 1]  
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.presm[row2 + 1][col2 + 1] - 
            self.presm[row1][col2 + 1] -  
            self.presm[row2 + 1][col1] +  
            self.presm[row1][col1]  
        )
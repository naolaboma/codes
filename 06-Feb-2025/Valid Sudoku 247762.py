# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_group(group):
            elements = [x for x in group if x != '.']
            return len(elements) == len(set(elements))
        
        # Check rows
        for row in board:
            if not is_valid_group(row):
                return False
        
        # Check columns
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not is_valid_group(column):
                return False
        
        # Check 3x3 sub-boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = [board[row][col] for row in range(box_row, box_row+3) 
                                        for col in range(box_col, box_col+3)]
                if not is_valid_group(box):
                    return False
        
        return True
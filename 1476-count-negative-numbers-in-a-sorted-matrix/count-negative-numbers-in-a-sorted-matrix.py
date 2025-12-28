class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        def binsearch(row):
            count = len(row)

            left = 0
            right = len(row)-1

            while left <= right:
                mid = left + (right -left)//2
                if row[mid] <0:
                    count = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return count
        for row in grid:
            count = binsearch(row)
            result += len(row) - count
        return result
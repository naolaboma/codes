# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
        def hasValidPath(self, grid: List[List[int]]) -> bool:
            m, n = len(grid), len(grid[0])
            
            # dict for transition rule
            rules = {
                1: {0: 0, 3: 3},
                2: {1: 1, 2: 2},
                3: {0: 2, 1: 3},
                4: {1: 0, 3: 2},
                5: {0: 1, 2: 3},
                6: {2: 0, 3: 1},
            }
            
            # dict for update rule
            moves = {
                0: (0, 1),
                1: (-1, 0),
                2: (1, 0),
                3: (0, -1),
            }
            
            x, y = (0, 0)
            k = grid[0][0]
            d = list(rules[k].keys())
            d1, d2 = d[0], d[1]
            
            def walkMaze(x, y, d):
                visited = set([(x, y)])
                while True:
                    if x < 0 or x >= m or y < 0 or y >= n:
                        return False
                    
                    k = grid[x][y]
                    if d not in rules[k]:
                        return False
                    
                    if (x, y) == (m - 1, n - 1):
                        return True
                    
                    d = rules[k][d]
                    x, y = (x + moves[d][0], y + moves[d][1])
                    if (x, y) in visited: # there is a loop
                        return False
                    visited.add((x, y))
            
            return walkMaze(x, y, d1) or walkMaze(x, y, d2)
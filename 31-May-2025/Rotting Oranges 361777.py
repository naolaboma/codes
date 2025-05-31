# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshy = 0
        time = 0
        m = len(grid)
        n = len(grid[0])

        q = deque()

        # Queue all rotten oranges and count fresh ones
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    freshy += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        # Run multi-source BFS
        while q:
            rotten_oranges = 0
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] == 1:

                        q.append((new_r, new_c))
                        grid[new_r][new_c] = 2
                        freshy -= 1
                        rotten_oranges += 1
            if rotten_oranges > 0:
                time += 1
        return time if freshy == 0 else -1
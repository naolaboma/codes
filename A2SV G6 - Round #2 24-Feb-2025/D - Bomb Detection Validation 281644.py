# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

def is_valid_field(n, m, field):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(n):
        for j in range(m):
            if field[i][j] == '.':
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m and field[ni][nj] == '*':
                        return "NO"
            elif field[i][j].isdigit():
                expected_bombs = int(field[i][j])
                actual_bombs = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m and field[ni][nj] == '*':
                        actual_bombs += 1
                if actual_bombs != expected_bombs:
                    return "NO"
    return "YES"
n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]
print(is_valid_field(n, m, field))
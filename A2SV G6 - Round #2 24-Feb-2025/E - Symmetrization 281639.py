# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

def min_operations_to_symmetrize(grid, n):
    operations = 0
    for i in range(n):
        for j in range(n):
            if i <= j and i < n - 1 - j:
                a = grid[i][j]
                b = grid[j][n - 1 - i]
                c = grid[n - 1 - i][n - 1 - j]
                d = grid[n - 1 - j][i]
                ones = int(a) + int(b) + int(c) + int(d)
                operations += min(ones, 4 - ones)
    return operations
t = int(input())
results = []
for _ in range(t):
    n = int(input())
    grid = [input().strip() for _ in range(n)]
    results.append(min_operations_to_symmetrize(grid, n))
print("\n".join(map(str, results)))
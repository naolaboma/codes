# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

def x_sum(t, test_cases):
    results = []
    for case in test_cases:
        n, m, grid = case
        diag1 = [0] * (n + m - 1) 
        diag2 = [0] * (n + m - 1)  
        for i in range(n):
            for j in range(m):
                diag1[i + j] += grid[i][j]
                diag2[i - j + (m - 1)] += grid[i][j]
        max_sum = 0
        for i in range(n):
            for j in range(m):
                cell_sum = diag1[i + j] + diag2[i - j + (m - 1)] - grid[i][j]
                max_sum = max(max_sum, cell_sum)
        results.append(max_sum)
    return results
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, m, grid))
results = x_sum(t, test_cases)
for res in results:
    print(res)
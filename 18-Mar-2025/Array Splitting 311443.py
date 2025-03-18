# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

def min_cost_split(n, k, arr):
    diffs = [arr[i] - arr[i - 1] for i in range(1, n)]
    diffs.sort(reverse=True)
    return arr[-1] - arr[0] - sum(diffs[:k-1])

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(min_cost_split(n, k, arr))
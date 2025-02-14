# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

def solve():
    t = int(input())  
    results = []
    for _ in range(t):
        n = int(input())  
        a = list(map(int, input().split()))
        max_val = a[0]
        sum_result = 0
        for i in range(1, n):
            if (a[i] > 0 and a[i - 1] > 0) or (a[i] < 0 and a[i - 1] < 0):
                max_val = max(max_val, a[i])
            else:
                sum_result += max_val
                max_val = a[i]
        sum_result += max_val
        results.append(sum_result)
    print("\n".join(map(str, results)))
solve()
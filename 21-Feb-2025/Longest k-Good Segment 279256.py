# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

n, k = map(int, input().split())
a = list(map(int, input().split()))
freq = {}
l = 0  
max_len = 0
best_l, best_r = 0, 0  
for r in range(n):  
    if a[r] in freq:
        freq[a[r]] += 1
    else:
        freq[a[r]] = 1
    while len(freq) > k:
        freq[a[l]] -= 1
        if freq[a[l]] == 0:
            del freq[a[l]]  
        l += 1
    if r - l + 1 > max_len:
        max_len = r - l + 1
        best_l, best_r = l, r
print(best_l + 1, best_r + 1)
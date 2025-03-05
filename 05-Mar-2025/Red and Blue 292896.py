# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    pres1 = 0
    pres2 = 0
    maxi = 0
    maxj = 0
    for i in range(n):
        pres1 += r[i]
        maxi= max(maxi, pres1)
    for j in range(m):
        pres2+=b[j]
        maxj = max(maxj, pres2)
    print(maxi + maxj)

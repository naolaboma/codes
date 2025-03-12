# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())
intt = list(map(int, input().split()))
m = int(input())
pro = [0] * (n + 1)
for i in range(1, n + 1):
    pro[i] = pro[i - 1] + intt[i - 1]
pfs = [0] * (n + 1)
sint = sorted(intt)


for i in range(1, n + 1):
    pfs[i] = pfs[i - 1] + sint[i - 1]

for _ in range(m):
    t, l, r = map(int, input().split())
    if t == 1:
        print(pro[r] - pro[l - 1])
    elif t == 2:
        print(pfs[r] - pfs[l - 1])
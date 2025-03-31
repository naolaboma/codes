# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = []
p1, p2 = 0, 0
while p1 <n or p2 <m:
    if p1 <n and p2 <m:
        if a[p1]< b[p2]:
            res.append(a[p1])
            p1+=1
        elif b[p2] < a[p1]:
            res.append(b[p2])
            p2+=1
        elif b[p2] == a[p1]:
            res.append(a[p1])
            res.append(b[p2])
            p1+=1
            p2+=1
    elif p1==n:
        res.append(b[p2])
        p2+=1
    elif p2 ==m:
        res.append(a[p1])
        p1+=1
print(*res)
# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = map(int, input().split())
a = list(map(int,input().split()))
l,r = 0,0
summ = 0
res = 0
while r<len(a):
    summ += a[r]
    while summ >s:
        summ -=a[l]
        l+=1
    res = max(res,r-l+1)
    r+=1
print(res)
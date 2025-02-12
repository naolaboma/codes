# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n, m = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = []
count=0
for i in range(m):
    while count < len(a) and a[count] < b[i]:
        count+=1
    res.append(count)
print(" ".join(map(str, res)))
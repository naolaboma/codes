# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
merged = []
f,s=0,0
while f < len(a) and s < len(b):
    if a[f]<b[s]:
        merged.append(a[f])
        f+=1
    else:
        merged.append(b[s])
        s+=1
merged.extend(a[f:])
merged.extend(b[s:])
print(" ".join(map(str,merged)))
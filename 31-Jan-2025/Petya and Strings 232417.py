# Problem: Petya and Strings - https://codeforces.com/problemset/problem/112/A

x = input()
y = input()
x = x.lower()
y = y.lower()
if x<y:
    print(-1)
elif x==y:
    print(0)
else:
    print(1)

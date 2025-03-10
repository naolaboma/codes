# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n = int(input())
x = list(map(int, input().split()))
x.sort()
print(x[(n - 1) //2])
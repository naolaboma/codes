# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

n = int(input())
t = str(input())
st = ""
l, r = 0, 0
while r < n:
    st+=t[r]
    l+=1
    r+=l
print(st)
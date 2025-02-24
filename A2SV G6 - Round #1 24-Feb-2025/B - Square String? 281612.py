# Problem: B - Square String? - https://codeforces.com/gym/585107/problem/B

t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    if n % 2 == 0 and s[:n//2] == s[n//2:]:
        print("YES")
    else:
        print("NO")
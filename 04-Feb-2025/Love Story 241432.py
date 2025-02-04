# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

reference = "codeforces"
t = int(input())
results = []
for _ in range(t):
    s = input().strip()
    differences = sum(1 for i in range(10) if s[i] != reference[i])
    results.append(differences)
print("\n".join(map(str, results)))
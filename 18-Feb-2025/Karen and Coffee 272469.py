# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

def karen_and_coffee(n, k, q, recipes, queries):
    MAX_TEMP = 200000
    temp = [0] * (MAX_TEMP + 2)
    for l, r in recipes:
        temp[l] += 1
        temp[r + 1] -= 1
    for i in range(1, MAX_TEMP + 1):
        temp[i] += temp[i - 1]
    admissible = [0] * (MAX_TEMP + 1)
    for i in range(1, MAX_TEMP + 1):
        admissible[i] = 1 if temp[i] >= k else 0
    for i in range(1, MAX_TEMP + 1):
        admissible[i] += admissible[i - 1]
    results = []
    for a, b in queries:
        results.append(admissible[b] - admissible[a - 1])
    print(*results, sep='\n')
n,k,q = map(int,input().split())
recipes = []
queries = []
for i in range(n):
    l,r = map(int, input().split())
    recipes.append([l,r])
for j in range(q):
    a,b = map(int, input().split())
    queries.append([a,b])
karen_and_coffee(n, k, q, recipes, queries)
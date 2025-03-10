# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())  
    a = list(map(int, input().split()))  
    b = list(map(int, input().split()))  
    
    a_sorted = sorted((val, idx) for idx, val in enumerate(a))  
    b.sort()  
    res = [0] * n 
    for (val, idx), temp in zip(a_sorted, b):
        res[idx] = temp  
    print(*res)  
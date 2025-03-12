# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    
    count = 0
    i = 0
    
    while i < n - 1:
        if nums[i] > nums[i + 1]:
            count += 1
            i += 2
        else:
            i += 1
    print(count)
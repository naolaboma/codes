# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

def max_equal_length(n, a, m, b):
    if sum(a) != sum(b):
        return -1
    i, j = 0, 0
    count = 0
    current_a, current_b = 0, 0
    while i < n and j < m:
        if current_a == 0 and current_b == 0:
            current_a += a[i]
            current_b += b[j]
            i += 1
            j += 1
        elif current_a < current_b:
            current_a += a[i]
            i += 1
        elif current_a > current_b:
            current_b += b[j]
            j += 1
        else:
            count += 1
            current_a, current_b = 0, 0
    while i < n:
        current_a += a[i]
        i += 1
    while j < m:
        current_b += b[j]
        j += 1
    if current_a == current_b:
        count += 1
    else:
        return -1
    return count
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
print(max_equal_length(n, a, m, b))
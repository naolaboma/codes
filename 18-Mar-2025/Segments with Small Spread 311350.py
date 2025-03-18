# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque

def solve(n, k, arr):
    left = 0
    count = 0
    mini, maxi = deque(), deque()

    for right in range(n):
        while mini and arr[mini[-1]] > arr[right]:
            mini.pop()
        while maxi and arr[maxi[-1]] < arr[right]:
            maxi.pop()

        mini.append(right)
        maxi.append(right)

        while arr[maxi[0]] - arr[mini[0]] > k:
            left += 1
            if mini[0] < left:
                mini.popleft()
            if maxi[0] < left:
                maxi.popleft()

        count += right - left + 1

    return count

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(solve(n, k, arr))

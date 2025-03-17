# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

from heapq import heappop, heappush

def solve():
    n = int(input())
    s = list(map(int, input().strip()))

    ones_heap, zeros_heap = [], []
    result = [0] * n
    total_groups = 1

    for idx, char in enumerate(s):
        if char == 1:
            if not ones_heap:
                heappush(ones_heap, total_groups)
                total_groups += 1
            current_group = heappop(ones_heap)
            heappush(zeros_heap, current_group)
        else:
            if not zeros_heap:
                heappush(zeros_heap, total_groups)
                total_groups += 1
            current_group = heappop(zeros_heap)
            heappush(ones_heap, current_group)
        result[idx] = current_group

    print(total_groups - 1)
    print(*result)

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        solve()
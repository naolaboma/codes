# Problem: F - Nahom's Array Dilemma - https://codeforces.com/gym/594077/problem/F

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    def prevGreater(nums):
        stack = []
        pref = [0]
        for num in nums:
            pref.append(pref[-1] + num)
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                v = stack.pop()
                if pref[i] - pref[v] > 0:
                    return False
            stack.append(i)
        return True
    if prevGreater(nums) and prevGreater(nums[::-1]):
        return "YES"
    return "NO"
t = int(input())
for _ in range(t):
    print(solve())
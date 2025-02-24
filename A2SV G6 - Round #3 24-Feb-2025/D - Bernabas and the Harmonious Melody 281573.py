# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

def is_palindrome(s):
    return s == s[::-1]
def min_removals(s):
    if is_palindrome(s):
        return 0
    min_removal = float('inf')
    for char in set(s):
        i, j = 0, len(s) - 1
        removals = 0
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif s[i] == char:
                i += 1
                removals += 1
            elif s[j] == char:
                j -= 1
                removals += 1
            else:
                removals = float('inf')
                break
        min_removal = min(min_removal, removals)
    return min_removal if min_removal != float('inf') else -1
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    result = min_removals(s)
    print(result)
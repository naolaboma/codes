# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

def can_transform(s, t, p):
    from collections import Counter
    if not is_subsequence(s, t):
        return False
    freq_s = Counter(s)
    freq_t = Counter(t)
    freq_p = Counter(p)
    for char in freq_t:
        if freq_t[char] > freq_s[char] + freq_p[char]:
            return False
    return True
def is_subsequence(s, t):
    it = iter(t)
    return all(c in it for c in s)
q = int(input())
results = []
for _ in range(q):
    s = input()
    t = input()
    p = input()
    results.append("YES" if can_transform(s, t, p) else "NO")
print("\n".join(results))
class Solution:
    def calc_z(self, s: str) -> List[int]:
        n = len(s)
        z = [0] * n
        box_l, box_r = 0, 0  # z-box boundaries
        for i in range(1, n):
            if i <= box_r:
                z[i] = min(z[i - box_l], box_r - i + 1)
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                box_l, box_r = i, i + z[i]
                z[i] += 1
        z[0] = n
        return z

    def generateString(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        ans = ['?'] * (n + m - 1)
        
        # Process 'T' with Z-function
        z = self.calc_z(t)
        pre = -m
        for i, b in enumerate(s):
            if b != 'T':
                continue
            size = max(pre + m - i, 0)
            # Prefix/Suffix overlap must be consistent
            if size > 0 and z[m - size] < size:
                return ""
            ans[i + size: i + m] = t[size:]
            pre = i
            
        # Precompute nearest pending positions
        pre_q = [-1] * len(ans)
        pre = -1
        for i, c in enumerate(ans):
            if c == '?':
                ans[i] = 'a'
                pre = i
            pre_q[i] = pre
            
        # Match ans against t using Z-function
        z = self.calc_z(t + ''.join(ans))
        
        # Process 'F'
        i = 0
        while i < n:
            if s[i] != 'F':
                i += 1
                continue
            if z[m + i] < m:
                i += 1
                continue
            # Modify the last pending position
            j = pre_q[i + m - 1]
            if j < i:
                return ""
            ans[j] = 'b'
            i = j + 1  # Optimization: skip past the modified index
        return ''.join(ans)
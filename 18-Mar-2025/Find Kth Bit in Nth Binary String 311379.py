# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def btn(n, k):

            if n == 1:
                return "0"
            leng = (1 << n) - 1
            mid = leng // 2 + 1
            if k == mid:
                return "1"
            elif k < mid:
                return btn(n - 1, k)
            else:
                return str(1 - int(btn(n - 1, leng - k + 1)))
        return btn(n, k)
# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for size in range(n, 1, -1):
            max_index = arr.index(max(arr[:size]))
            if max_index == size - 1:
                continue
            if max_index != 0:
                res.append(max_index + 1)
                arr[:max_index + 1] = reversed(arr[:max_index + 1])
            res.append(size)
            arr[:size] = reversed(arr[:size])
        return res
# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        maxi = max(c.values())
        buckets = [[] for _ in range(maxi + 1)]
        for num, freq in c.items():
            buckets[freq].append(num)
        res = []
        for i in range(maxi, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

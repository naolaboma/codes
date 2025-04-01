# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = defaultdict(int)
        for rpet in nums:
            c[rpet]+=1
        output = []
        st = dict(sorted(c.items(), key = lambda item : item[1], reverse = True))
        for ke, v in st.items():
            output.append(ke)
        return output[:k]
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        max_heap = [-h for h in happiness]
        heapq.heapify(max_heap)
        total_happiness_sum = 0
        turns = 0
        for i in range(k):
            total_happiness_sum += max(-heapq.heappop(max_heap) - turns, 0)
            turns += 1
        return total_happiness_sum

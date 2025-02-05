# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(num for num in nums if num % 2 == 0)
        answer = []
        for val, index in queries:
            original_value = nums[index]
            if original_value % 2 == 0:
                even_sum -= original_value
            nums[index] += val
            updated_value = nums[index]
            if updated_value % 2 == 0:
                even_sum += updated_value
            answer.append(even_sum)

        return answer
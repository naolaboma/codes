# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxDeque = deque()
        minDeque = deque()
        left = 0
        result = 0 
        for right in range(len(nums)):
            while maxDeque and nums[maxDeque[-1]] <= nums[right]:
                maxDeque.pop()
            maxDeque.append(right)
            while minDeque and nums[minDeque[-1]] >= nums[right]:
                minDeque.pop()
            minDeque.append(right)
            while nums[maxDeque[0]] - nums[minDeque[0]] > limit:
                left += 1
                if maxDeque[0] < left:
                    maxDeque.popleft()
                if minDeque[0] < left:
                    minDeque.popleft()
            result = max(result, right - left + 1)
        return result
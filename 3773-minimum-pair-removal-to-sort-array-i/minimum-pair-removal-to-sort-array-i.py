class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def summ(nums):
            i, j = 0, 1
            plch = float('inf')
            ans = [plch, i, j]
            while j<len(nums):
                if plch > nums[i]+nums[j]:
                    plch = nums[i] + nums[j]
                    ans = [plch, i, j]
                i +=1
                j +=1
            return ans
        def replace(nums, ans):
            nums[ans[1]] = ans[0]
            nums.pop(ans[2])
        count = 0
        while nums != sorted(nums):
            ans = summ(nums)
            replace(nums, ans)
            count += 1
        return count


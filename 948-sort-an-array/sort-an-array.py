class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        OFFSET = 50000  # shift negatives to zero index
        SIZE = 100001   # from -50000 to 50000 inclusive

        count = [0] * SIZE

        # count frequencies
        for num in nums:
            count[num + OFFSET] += 1

        # rebuild sorted array
        i = 0
        for val in range(SIZE):
            freq = count[val]
            if freq:
                actual_val = val - OFFSET
                for _ in range(freq):
                    nums[i] = actual_val
                    i += 1

        return nums
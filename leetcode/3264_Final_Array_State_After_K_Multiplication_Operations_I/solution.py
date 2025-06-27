class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        for op in range(k):
            min_idx = 0
            min_val = nums[0]
            for i in range(1, n):
                if nums[i] < min_val:
                    min_idx = i
                    min_val = nums[i]
            nums[min_idx] *= multiplier
        return nums

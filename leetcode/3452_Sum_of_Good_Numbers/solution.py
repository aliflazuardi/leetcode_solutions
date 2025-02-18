class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        sum = 0
        l = len(nums)

        for i, n in enumerate(nums):
            is_left = (i - k < 0) or (nums[i - k] < n)
            is_right = (i + k >= l) or (nums[i + k] < n)

            if is_left and is_right:
                sum += n

        return sum

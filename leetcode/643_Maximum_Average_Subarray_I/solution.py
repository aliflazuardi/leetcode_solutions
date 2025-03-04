class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        for i in range(k):
            s += nums[i]
        max_avg = s / k

        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            max_avg = max(max_avg, (s / k))

        return max_avg

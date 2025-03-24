class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ps = [0] * len(nums)
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            ps[i] = s

        for i in range(len(ps)):
            if ps[i] - nums[i] == s - ps[i]:
                return i

        return -1

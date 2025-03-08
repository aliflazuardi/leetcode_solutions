class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_ones = 0
        l = 0
        r = 0
        zc = 0
        oc = 0

        while r < len(nums):
            if nums[r] == 0:
                zc += 1
                if zc > k:
                    while l < r and nums[l] != 0:
                        l += 1
                        oc -= 1
                    l += 1
                    zc -= 1
                    r += 1
                    continue
            oc += 1
            r += 1
            max_ones = max(max_ones, oc)

        return max_ones

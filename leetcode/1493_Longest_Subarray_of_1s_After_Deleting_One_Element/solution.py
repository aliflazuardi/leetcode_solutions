class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_o = 0
        l = 0
        r = 0
        o = 0
        z = False

        while r < len(nums):
            if nums[r] == 0:
                if z:
                    while l < r and nums[l] != 0:
                        l += 1
                        o -= 1
                    l += 1
                z = True
                r += 1
                continue
            o += 1
            r += 1
            max_o = max(max_o, o)

        if not z:
            max_o -= 1

        return max_o

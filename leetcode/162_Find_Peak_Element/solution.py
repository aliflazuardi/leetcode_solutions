class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            if nums[1] > nums[0]:
                return 1
            else:
                return 0

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            # check edges
            if m == len(nums) - 1 and nums[m] > nums[m - 1]:
                return m
            elif m == 0 and nums[m] > nums[m + 1]:
                return m

            # check if m is peak
            if (
                m != 0
                and nums[m] > nums[m + 1]
                and m != len(nums) - 1
                and nums[m] > nums[m - 1]
            ):
                return m

            # check if right is greater
            if nums[m + 1] > nums[m]:
                l = m + 1
            else:
                r = m - 1

        return 0

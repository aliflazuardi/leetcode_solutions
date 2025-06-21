class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        c = 0
        t = 0

        for i in range(len(nums)):
            if nums[i] != t:
                t = nums[i]
                c = 1
            else:
                c += 1
            if c > 2:
                continue
            nums[k] = t
            k += 1

        return k

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0

        while z < len(nums) - 1:
            while z < len(nums) - 1 and nums[z] != 0:
                z += 1
            p = z
            while p < len(nums) - 1 and nums[p] == 0:
                p += 1
            temp = nums[z]
            nums[z] = nums[p]
            nums[p] = temp

            z += 1

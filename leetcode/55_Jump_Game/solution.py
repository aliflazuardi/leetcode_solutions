class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums) != 1:
            return False

        jump_dist = nums[0] - 1
        i = 1

        while i < len(nums) - 1:
            jump_dist = max(jump_dist, nums[i])

            if jump_dist == 0:
                return False
            jump_dist -= 1
            i += 1

        return True

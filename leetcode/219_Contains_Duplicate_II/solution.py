class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx_map = {}

        for i in range(len(nums)):
            if nums[i] in idx_map:
                if i - idx_map[nums[i]] <= k:
                    return True
            idx_map[nums[i]] = i

        return False

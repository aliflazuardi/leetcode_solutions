class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        m = {}

        count = 0
        for num in nums:
            if num in m:
                count += m[num]
                m[num] += 1
                continue
            m[num] = 1

        return count

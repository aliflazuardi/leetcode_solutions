class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        pq = []

        for i in range(len(nums)):
            heapq.heappush(pq, (nums[i], i))

        ans = [0] * len(nums)
        prev_num = 0
        j = 0
        for i in range(len(nums)):
            num, idx = heapq.heappop(pq)
            if num == prev_num:
                ans[idx] = j
            else:
                ans[idx] = i
                j = i
            prev_num = num

        return ans

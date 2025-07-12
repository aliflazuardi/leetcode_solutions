class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        ans = []
        
        while nums:
            temp = heapq.heappop(nums)
            ans.append(heapq.heappop(nums))
            ans.append(temp)
        
        return ans

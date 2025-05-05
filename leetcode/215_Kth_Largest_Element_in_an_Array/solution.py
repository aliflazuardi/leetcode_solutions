class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, -1 * num)

        kth_elem = 0
        for i in range(k):
            kth_elem = -heapq.heappop(heap)

        return kth_elem

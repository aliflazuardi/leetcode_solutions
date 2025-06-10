class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pq = []

        n = len(heights)
        for i in range(n):
            heapq.heappush(pq, (-1 * heights[i], i))

        ans = []
        for i in range(n):
            h, i = heapq.heappop(pq)
            ans.append(names[i])

        return ans

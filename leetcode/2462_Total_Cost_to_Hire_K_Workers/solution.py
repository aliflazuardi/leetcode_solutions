class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        cost = 0
        n = len(costs)
        l = 0
        r = n - 1

        pq = []

        while l <= r and l < candidates:
            heapq.heappush(pq, (costs[l], l, True))
            l += 1

        count = 0
        while l <= r and count < candidates:
            heapq.heappush(pq, (costs[r], r, False))
            r -= 1
            count += 1

        while k > 0:
            c, i, is_left = heapq.heappop(pq)

            if l <= r:
                if is_left:
                    heapq.heappush(pq, (costs[l], l, True))
                    l += 1
                else:
                    heapq.heappush(pq, (costs[r], r, False))
                    r -= 1

            k -= 1
            cost += c

        return cost

class SmallestInfiniteSet:
    def __init__(self):
        self.n = 1
        self.pq = []
        self.added = set()

    def popSmallest(self) -> int:
        if len(self.pq) > 0 and self.pq[0] < self.n:
            ret = heapq.heappop(self.pq)
            self.added.remove(ret)
            return ret

        ret = self.n
        self.n += 1
        return ret

    def addBack(self, num: int) -> None:
        if num < self.n and num not in self.added:
            self.added.add(num)
            heapq.heappush(self.pq, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

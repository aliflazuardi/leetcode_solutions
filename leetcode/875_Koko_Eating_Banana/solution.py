class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        k = 0
        while l <= r:
            m = l + (r - l) // 2

            if self.isPossibleToEat(m, piles, h):
                r = m - 1
                k = m
            else:
                l = m + 1

        return k

    def isPossibleToEat(self, speed, piles, h):
        for pile in piles:
            h -= ceil(pile / speed)
            if h < 0:
                return False

        return True

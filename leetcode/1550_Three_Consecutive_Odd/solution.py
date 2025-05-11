class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_count = 0

        for v in arr:
            if v % 2 == 0:
                odd_count = 0
                continue
            if odd_count == 2:
                return True
            odd_count += 1

        return False

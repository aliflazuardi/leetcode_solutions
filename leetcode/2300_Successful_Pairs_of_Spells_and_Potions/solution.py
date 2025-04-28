class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()

        ans = []
        for i in range(len(spells)):
            l = 0
            r = len(potions) - 1
            min_successful_idx = -1

            while l <= r:
                m = l + (r - l) // 2

                if potions[m] * spells[i] >= success:
                    min_successful_idx = m
                    r = m - 1
                else:
                    l = m + 1

            if min_successful_idx >= 0:
                ans.append(len(potions) - min_successful_idx)
            else:
                ans.append(0)

        return ans

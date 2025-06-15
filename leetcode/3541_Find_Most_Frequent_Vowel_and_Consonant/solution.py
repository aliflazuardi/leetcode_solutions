class Solution:
    def maxFreqSum(self, s: str) -> int:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
                continue
            d[c] = 1

        max_v = 0
        max_c = 0
        for k, v in d.items():
            if k in ["a", "i", "u", "e", "o"]:
                max_v = max(max_v, v)
            else:
                max_c = max(max_c, v)

        return max_v + max_c

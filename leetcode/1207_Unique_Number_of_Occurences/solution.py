class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}

        for n in arr:
            if n not in count:
                count[n] = 1
                continue

            count[n] += 1

        freq = {}
        for k, v in count.items():
            if v in freq:
                return False
            freq[v] = k

        return True

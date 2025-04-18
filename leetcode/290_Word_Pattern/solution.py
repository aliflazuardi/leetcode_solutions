class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w = s.split()
        if len(pattern) != len(w):
            return False

        d = {}
        ws = set()

        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]] != w[i]:
                    return False
                continue
            if w[i] in ws:
                return False

            d[pattern[i]] = w[i]
            ws.add(w[i])

        return True

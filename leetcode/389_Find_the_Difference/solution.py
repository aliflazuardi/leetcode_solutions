class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sd = {}
        td = {}

        for i in range(len(s)):
            if s[i] not in sd:
                sd[s[i]] = 1
                continue
            sd[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in td:
                td[t[i]] = 1
                continue
            td[t[i]] += 1

        for k, v in td.items():
            if k not in sd or sd[k] != v:
                return k

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        d1 = {}
        d2 = {}
        for w in word1:
            if w in d1:
                d1[w] += 1
            else:
                d1[w] = 1
        for w in word2:
            if w in d2:
                d2[w] += 1
            else:
                d2[w] = 1

        c = {}
        for k in d1:
            if k not in d2:
                return False
            if d1[k] in c:
                c[d1[k]] += 1
            else:
                c[d1[k]] = 1

            if d2[k] in c:
                c[d2[k]] -= 1
            else:
                c[d2[k]] = -1

        for v in c.values():
            if v != 0:
                return False

        return True

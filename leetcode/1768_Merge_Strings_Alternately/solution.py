class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = max(len(word1), len(word2))

        w = ""
        for i in range(l):
            if i >= len(word1):
                w += word2[i:l]
                break
            if i >= len(word2):
                w += word1[i:l]
                break
            w += word1[i]
            w += word2[i]

        return w

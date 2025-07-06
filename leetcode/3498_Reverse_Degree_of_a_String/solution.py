class Solution:
    def reverseDegree(self, s: str) -> int:
        degree = 0
        for i in range(len(s)):
            degree += (123 - ord(s[i])) * (i + 1)

        return degree

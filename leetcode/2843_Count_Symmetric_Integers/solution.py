class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for x in range(low, high + 1):
            s = str(x)
            if len(s) % 2 != 0:
                continue

            n = int(len(s) / 2)
            x1 = s[0:n]
            x2 = s[n : 2 * n]

            s1 = 0
            s2 = 0
            for i in range(n):
                s1 += int(x1[i])
                s2 += int(x2[i])
            if s1 == s2:
                count += 1

        return count

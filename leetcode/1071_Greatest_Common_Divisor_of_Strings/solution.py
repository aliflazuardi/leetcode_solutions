class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 + str2 == str2 + str1:
            return ""

        gcd_index = gcd(len(str1), len(str2))
        return str1[0:gcd_index]


def gcd(l1, l2):
    if l2 == 0:
        return l1
    return gcd(l2, l1 % l2)

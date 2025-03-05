class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_count = 0
        for i in range(k):
            if is_vowel(s[i]):
                max_count += 1

        l = len(s)

        i = k
        c = max_count
        for i in range(k, l):
            if is_vowel(s[i - k]):
                c -= 1
            if is_vowel(s[i]):
                c += 1
            max_count = max(max_count, c)

        return max_count


def is_vowel(char):
    return char in {"a", "e", "i", "o", "u"}

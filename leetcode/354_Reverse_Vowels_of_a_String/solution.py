class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ""
        for c in s:
            if is_vowel(c):
                vowels += c

        ret = ""
        j = len(vowels) - 1
        for c in s:
            if is_vowel(c):
                ret = ret + vowels[j]
                j -= 1
                continue
            ret = ret + c

        return ret


def is_vowel(char):
    return char.lower() in {"a", "e", "i", "o", "u"}

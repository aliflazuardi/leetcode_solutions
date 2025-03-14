class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        ans = ""
        for word in reversed(words):
            ans += word + " "

        return ans[:-1]

class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            x = ord(s[i])
            if x >= 65 and x <= 90:
                ans += chr(x + 32)
            else:
                ans += s[i]

        return ans

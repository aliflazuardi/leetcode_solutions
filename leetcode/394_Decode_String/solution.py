class Solution:
    def decodeString(self, s: str) -> str:
        d = deque()

        decoded = ""
        i = len(s) - 1
        while i >= 0:
            if s[i] == "]":
                d.append(decoded)
                decoded = ""
                i -= 1
                continue

            if s[i] == "[":
                i -= 1
                m = 1
                r = 0
                while s[i].isnumeric():
                    r += int(s[i]) * m
                    m *= 10
                    i -= 1
                decoded = r * decoded
                decoded = decoded + d.pop()
                continue

            decoded = s[i] + decoded

            i -= 1

        return decoded

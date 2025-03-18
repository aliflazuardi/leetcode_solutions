class Solution:
    def compress(self, chars: List[str]) -> int:
        t = chars[0]
        cnt = 0
        s = ""
        for c in chars:
            if c == t:
                cnt += 1
                continue
            s += t
            if cnt != 1:
                s += str(cnt)
            t = c
            cnt = 1
        s += c
        if cnt != 1:
            s += str(cnt)

        for i, c in enumerate(s):
            chars[i] = c

        return len(s)

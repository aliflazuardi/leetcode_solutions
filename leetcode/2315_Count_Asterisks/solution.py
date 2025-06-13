class Solution:
    def countAsterisks(self, s: str) -> int:
        ans = 0
        is_between_pair = False

        for c in s:
            if c == "*" and not is_between_pair:
                ans += 1
            elif c == "|":
                is_between_pair = not is_between_pair

        return ans

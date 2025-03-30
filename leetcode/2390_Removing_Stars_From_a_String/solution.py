class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()

        for c in s:
            if c == "*":
                stack.pop()
                continue
            stack.append(c)

        ans = ""
        while stack:
            ans = stack.pop() + ans

        return ans

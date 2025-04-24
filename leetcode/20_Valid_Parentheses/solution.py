class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
                continue
            if len(stack) == 0:
                return False
            pair = stack.pop()
            if not (
                (pair == "(" and c == ")")
                or (pair == "{" and c == "}")
                or (pair == "[" and c == "]")
            ):
                return False

        return len(stack) == 0

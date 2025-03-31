class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        left = deque()
        right = deque()

        for asteroid in asteroids:
            if asteroid > 0:
                right.append(asteroid)
                continue

            is_break = False
            if len(right) > 0:
                while len(right) > 0:
                    right_ast = right[-1]
                    if right_ast < abs(asteroid):
                        right.pop()
                    elif right_ast == abs(asteroid):
                        right.pop()
                        is_break = True
                        break
                    else:
                        is_break = True
                        break

            if not is_break:
                left.append(asteroid)

        ans = []
        while left:
            ans.append(left.popleft())
        while right:
            ans.append(right.popleft())

        return ans

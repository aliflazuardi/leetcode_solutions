class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # DFS Solution
        n = len(isConnected)
        if n == 1:
            return 1
        stack = deque()
        visited = set()
        count = 0

        for i in range(n):
            if i in visited:
                continue
            visited.add(i)

            stack.append(i)
            while stack:
                c = stack.pop()
                for j in range(n):
                    if j in visited or isConnected[c][j] == 0:
                        continue
                    stack.append(j)
                    visited.add(j)
            count += 1

        return count

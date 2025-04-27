class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        stack = deque()
        visited = [False] * n
        roads = {}
        for connection in connections:
            if connection[0] in roads:
                roads[connection[0]].append(connection[1])
            else:
                roads[connection[0]] = [connection[1]]

            if connection[1] in roads:
                roads[connection[1]].append(-1 * connection[0])
            else:
                roads[connection[1]] = [-1 * connection[0]]

        stack.append(0)
        visited[0] = True
        reorder_count = 0

        while stack:
            c = stack.pop()
            for p in roads[c]:
                if visited[abs(p)]:
                    continue

                if p > 0:
                    reorder_count += 1

                stack.append(abs(p))
                visited[abs(p)] = True

        return reorder_count

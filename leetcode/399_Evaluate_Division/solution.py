class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = {}

        for i in range(len(equations)):
            if equations[i][0] in graph:
                graph[equations[i][0]].append((equations[i][1], values[i]))
            else:
                graph[equations[i][0]] = [(equations[i][1], values[i])]

            if equations[i][1] in graph:
                graph[equations[i][1]].append((equations[i][0], 1 / values[i]))
            else:
                graph[equations[i][1]] = [(equations[i][0], 1 / values[i])]

        print(graph)
        ans = []

        for i in range(len(queries)):
            if queries[i][0] not in graph or queries[i][1] not in graph:
                ans.append(-1.0)
                continue
            if queries[i][0] == queries[i][1]:
                ans.append(1.0)
                continue

            stack = deque()

            stack.append((queries[i][0], queries[i][1], 1))

            is_found = False
            visited = {queries[i][0]}
            while stack and not is_found:
                c, d, v = stack.pop()

                values = graph[c]
                for val in values:
                    a, b = val
                    if a in visited:
                        continue
                    visited.add(a)
                    eq = v * b
                    if a == d:
                        ans.append(eq)
                        is_found = True
                        break
                    stack.append((a, d, eq))
            if not is_found:
                ans.append(-1.0)

        return ans

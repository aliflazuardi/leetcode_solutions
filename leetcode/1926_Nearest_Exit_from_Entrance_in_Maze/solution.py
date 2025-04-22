class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()
        visited = set()

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        queue.append((entrance, 0))
        visited.add((entrance[0], entrance[1]))

        while queue:
            coordinates, dist = queue.popleft()
            x = coordinates[0]
            y = coordinates[1]

            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                if (
                    0 <= next_x < len(maze)
                    and 0 <= next_y < len(maze[0])
                    and (next_x, next_y) not in visited
                    and maze[next_x][next_y] == "."
                ):
                    if (
                        next_x == 0
                        or next_x == len(maze) - 1
                        or next_y == 0
                        or next_y == len(maze[0]) - 1
                    ):
                        return dist + 1
                    queue.append(([x + dx[i], y + dy[i]], dist + 1))
                    visited.add((x + dx[i], y + dy[i]))

        return -1

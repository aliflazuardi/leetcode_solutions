class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        keys = deque()
        keys.append(0)

        while keys:
            key = keys.pop()
            visited.add(key)
            new_keys = rooms[key]
            for k in new_keys:
                if k not in visited:
                    keys.append(k)

        return len(visited) == len(rooms)

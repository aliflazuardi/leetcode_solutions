class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        elems = {}

        n = len(grid)

        for i in range(n):
            elem = ""
            for j in range(n):
                elem += str(grid[i][j]) + ","
            if elem in elems:
                elems[elem] += 1
            else:
                elems[elem] = 1

        c = 0
        for i in range(n):
            elem = ""
            for j in range(n):
                elem += str(grid[j][i]) + ","
            if elem in elems:
                c += elems[elem]

        return c

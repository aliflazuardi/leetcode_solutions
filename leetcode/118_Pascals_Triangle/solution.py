class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        i = 2
        while i <= numRows:
            l = [1] * i
            j = 1
            while j < i - 1:
                l[j] = result[i - 2][j - 1] + result[i - 2][j]
                j += 1

            result.append(l)
            i += 1

        return result

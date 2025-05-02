class Solution:
    memory = [0, 1, 1]

    def tribonacci(self, n: int) -> int:
        if n == 0 or (n < len(self.memory) and self.memory[n] != 0):
            return self.memory[n]

        res = self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)
        self.memory.append(res)
        return res

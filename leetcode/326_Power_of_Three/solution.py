class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n % 2 == 0 or n <= 0:
            return False
        if n == 1:
            return True
        return self.isPowerOfThree(n / 3)

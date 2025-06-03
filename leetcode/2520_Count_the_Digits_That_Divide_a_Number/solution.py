class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0

        nums = num
        while nums > 0:
            val = nums % 10
            if num % val == 0:
                ans += 1
            nums = nums // 10

        return ans

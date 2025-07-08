class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        once = set()
        twice = set()

        for num in nums:
            if num in once:
                twice.add(num)
                continue
            once.add(num)

        ans = 0
        for n in twice:
            ans ^= n

        return ans

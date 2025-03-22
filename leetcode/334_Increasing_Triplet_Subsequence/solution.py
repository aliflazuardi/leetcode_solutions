class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = sys.maxsize
        second = sys.maxsize

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True

        return False

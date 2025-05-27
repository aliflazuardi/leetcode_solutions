class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        s = set()

        for num in nums:
            if num in s:
                ans.append(num)
                if len(ans) == 2:
                    break
                continue
            s.add(num)

        return sorted(ans)

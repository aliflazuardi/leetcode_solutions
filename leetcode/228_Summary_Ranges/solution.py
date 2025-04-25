class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        ans = []

        c = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != prev + 1:
                if c == 1:
                    ans.append(f"{prev}")
                else:
                    ans.append(f"{prev - c + 1}->{prev}")
                c = 1
                prev = nums[i]
                continue
            prev = nums[i]
            c += 1

        if c == 1:
            ans.append(f"{prev}")
        else:
            ans.append(f"{prev - c + 1}->{prev}")

        return ans

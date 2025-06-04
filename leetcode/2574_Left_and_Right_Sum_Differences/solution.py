class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix_sum = [nums[0]]
        total_sum = nums[0]

        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i - 1] + nums[i])
            total_sum += nums[i]

        answer = [total_sum - prefix_sum[0]]

        for i in range(1, len(nums)):
            answer.append(abs(prefix_sum[i - 1] - (total_sum - prefix_sum[i])))

        return answer

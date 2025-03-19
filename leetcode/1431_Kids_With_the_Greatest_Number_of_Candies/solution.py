class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = 0
        for candy in candies:
            max_candy = max(max_candy, candy)
        tresh = max_candy - extraCandies

        ans = [True] * len(candies)
        for i in range(len(candies)):
            if candies[i] < tresh:
                ans[i] = False

        return ans

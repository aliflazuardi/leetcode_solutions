class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set()

        for jewel in jewels:
            jewels_set.add(jewel)

        jewel_stone_count = 0

        for stone in stones:
            if stone in jewels_set:
                jewel_stone_count += 1

        return jewel_stone_count

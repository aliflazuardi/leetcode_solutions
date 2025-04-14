class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(0, len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    if isGoodTriplets(arr[i], arr[j], arr[k], a, b, c):
                        count += 1

        return count


def isGoodTriplets(i_val, j_val, k_val, a, b, c):
    if abs(i_val - j_val) > a:
        return False
    if abs(j_val - k_val) > b:
        return False
    if abs(i_val - k_val) > c:
        return False

    return True

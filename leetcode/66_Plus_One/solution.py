class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        digits[-1] = 0
        i = len(digits) - 2
        if i < 0:
            return [1, 0]

        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    return digits
                i -= 1
                continue
            digits[i] += 1
            break

        return digits

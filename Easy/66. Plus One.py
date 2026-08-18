class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        index = len(digits) - 1
        while index >= 0:
            if digits[index] != 9:
                digits[index] += 1
                return digits
            digits[index] = 0
            index -= 1
        return [1] + digits
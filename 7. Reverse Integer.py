class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        rev_x = 0
        if x < 0:
            x = -1 * x
            negative = True
        while x != 0:
            rev_x = rev_x * 10 + x % 10
            x = x // 10
        if rev_x > (2**(31) - 1):
                    return 0
        if negative:
            rev_x = rev_x * -1
        return rev_x
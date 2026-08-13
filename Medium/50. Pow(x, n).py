class Solution:
    def myPow(self, x: float, n: int) -> float:
        exp = x
        output = 1
        if n < 0:
            n = -1 * n
            exp = 1 / exp
        while n != 0:
            if ((n & 1) != 0):
                output = output * exp
            n = n // 2
            exp = exp * exp
        return output
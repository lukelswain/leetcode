class Solution:
    def isPalindrome(self, x: int) -> bool:
        int_list = [i for i in str(x)]
        return int_list == int_list[::-1]

class Solution2:
    def isPalindrome(self, x:int) -> bool:
        if x < 0:
            return False
        initial_x = x
        rev_x = 0
        while x != 0:
            rev_x = rev_x * 10 + x % 10
            x = x // 10
        return initial_x == rev_x
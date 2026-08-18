class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s)-1
        count = 0
        while index >= 0:
            if s[index] == ' ':
                if count != 0:
                    break
                else:
                    count -= 1
            count += 1
            index -= 1
        return count
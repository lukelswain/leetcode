class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        while index < len(haystack)-len(needle)+1:
            if haystack[index:index + len(needle)] == needle:
                return index
            index += 1
        return -1
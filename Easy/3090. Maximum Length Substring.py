class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        if len(s) < 3:
            return len(s)
        char_count = {}
        max_substring = s[0:2]
        current_substring = s[0:2]
        for char in current_substring:
            if char in char_count:
                char_count[char] += 1
                continue
            char_count[char] = 1
        i = 2
        while i < len(s):
            current_substring += s[i]
            if s[i] in char_count:
                char_count[s[i]] += 1
                if char_count[s[i]] > 2:
                    while char_count[s[i]] > 2:
                        char_count[current_substring[0]] -= 1
                        current_substring = current_substring[1:]
            else:
                char_count[s[i]] = 1
            if len(current_substring) > len(max_substring):
                max_substring = current_substring
            i += 1
        return len(max_substring)

sol = Solution()
print(sol.maximumLengthSubstring('eebadadbfa'))
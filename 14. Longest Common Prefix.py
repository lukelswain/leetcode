class Solution:
    def longestCommonPrefix(self, strs:list[str]) -> str:
        lcp = ''
        end_loop = False
        i = 0
        while not end_loop:
            for j in range(len(strs)):
                if (i+1) > len(strs[j]):
                    end_loop = True
                    break
                if (j > 0) and (strs[j][i] != strs[j-1][i]):
                    end_loop = True
                    break
            if not end_loop:
                lcp = lcp + strs[0][i]
                i += 1
        return lcp
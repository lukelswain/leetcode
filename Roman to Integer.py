class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0
        while s != '':
            if len(s) == 1:
                if s == 'I':
                    integer += 1
                if s == 'V':
                    integer += 5
                if s == 'X':
                    integer += 10
                if s == 'L':
                    integer += 50
                if s == 'C':
                    integer += 100
                if s == 'D':
                    integer += 500
                if s == 'M':
                    integer += 1000
                s = ''
                continue
            if s[-1] == 'I':
                integer += 1
                s = s[0:-1]
                continue
            if s[-1] == 'V':
                if s[-2] == 'I':
                    integer += 4
                    s = s[0:-2]
                    continue
                else:
                    integer += 5
                    s = s[0:-1]
                    continue
            if s[-1] == 'X':
                if s[-2] == 'I':
                    integer += 9
                    s = s[0:-2]
                    continue
                else:
                    integer += 10
                    s = s[0:-1]
                    continue
            if s[-1] == 'L':
                if s[-2] == 'X':
                    integer += 40
                    s = s[0:-2]
                    continue
                else:
                    integer += 50
                    s = s[0:-1]
                    continue
            if s[-1] == 'C':
                if s[-2] == 'X':
                    integer += 90
                    s = s[0:-2]
                    continue
                else:
                    integer += 100
                    s = s[0:-1]
                    continue
            if s[-1] == 'D':
                if s[-2] == 'C':
                    integer += 400
                    s = s[0:-2]
                    continue
                else:
                    integer += 500
                    s = s[0:-1]
                    continue
            if s[-1] == 'M':
                if s[-2] == 'C':
                    integer += 900
                    s = s[0:-2]
                    continue
                else:
                    integer += 1000
                    s = s[0:-1]
                    continue   
        return integer
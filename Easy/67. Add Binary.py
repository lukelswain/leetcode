class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            temp = a
            a = b
            b = temp
        pointer_b = len(b) - 1
        pointer_a = len(a) - 1
        carry = '0'
        output = ''
        while pointer_a >= 0 or pointer_b >= 0:
            if pointer_a < 0:
                a_val = '0'
                b_val = b[pointer_b]
            elif pointer_b < 0:
                b_val = '0'
                a_val = a[pointer_a]
            else:
                a_val = a[pointer_a]
                b_val = b[pointer_b]
            if carry == '0':
                if a_val == '1' and b_val == '1':
                    output = '0' + output
                    carry = '1'
                elif a_val == '1' or b_val == '1':
                    output = '1' + output
                else:
                    output = '0' + output
            else:
                if a_val == '1' and b_val == '1':
                    output = '1' + output
                    carry = '1'
                elif a_val == '1' or b_val == '1':
                    output = '0' + output
                    carry = '1'
                else:
                    output = '1' + output
                    carry = '0'
            pointer_a -= 1
            pointer_b -= 1
        if carry == '1':
            return '1' + output
        return output

sol = Solution()
a = '111'
b = '1'
print(sol.addBinary(a, b))
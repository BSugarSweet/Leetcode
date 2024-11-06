class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n_a = len(a)
        n_b = len(b)
        ans = ""
        carry = 0

        if n_a > n_b:
            b = "0" * (n_a - n_b) + b
        else:
            a = "0" * (n_b - n_a) + a

        for i in range(len(a) - 1, -1, -1):
            s = carry ^ (int(a[i]) ^ int(b[i]))
            carry = (int(a[i]) & int(b[i])) | (carry & (int(a[i]) ^ int(b[i])))
            ans += str(s)
        if carry:
            ans += "1"
        ans = ans[::-1]
        return ans
        
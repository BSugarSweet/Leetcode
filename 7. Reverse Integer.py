class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        n = len(s)
        res = ""

        if s[0] == '-':
            s = s[0] + s[n-1:0:-1]
            if int(s) < -2 ** 31:
                return 0
            return int(s)
        s = s[-1::-1]
        if int(s) >= 2 ** 31:
            return 0
        return int(s)
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        total = 0
        res = []
        
        if k == 0:
            return [0] * n

        for i in range(n):
            code.append(code[i])
        
        if k > 0:
            for i in range(1,k+1):
                total += code[i]
            res.append(total)
            for i in range(k+1, n+k):
                total -= code[i-k]
                total += code[i]
                res.append(total)
            return res

        if k < 0:
            k = -k
            for i in range(n-k, n):
                total += code[i]
            res.append(total)
            for i in range(n, len(code) - 1):
                total -= code[i-k]
                total += code[i]
                res.append(total)
            return res

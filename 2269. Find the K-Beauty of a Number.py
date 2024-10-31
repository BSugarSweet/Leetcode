class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        str_num = str(num)
        n = len(str_num)
        ans = 0 
        tmp = str_num[:k]
        
        if int(tmp) != 0 and num % int(tmp) == 0:
            ans += 1
        
        for i in range(k,n):
            tmp = tmp[1:]
            tmp += str_num[i]
            if int(tmp) != 0 and num % int(tmp) == 0:
                ans += 1
        return ans

        
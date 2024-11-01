class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[0]
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i-1] and count == 2:
                continue
            if s[i] == s[i-1] and count == 1:
                count += 1
                ans += s[i]
                continue
            count = 1
            ans += s[i]
        return ans            
        
class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        first = "qwertyuiopQWERTYUIOP"
        second = "asdfghjklASDFGHJKL"
        third = "zxcvbnmZXCVBNM"
        confirm = True
        ans = []
        
        for s in words:
            confirm = True
            if s[0] in first:
                for i in range(1, len(s)):
                    if s[i] not in first:
                        confirm = False
                        break
                if confirm:
                    ans.append(s)
            elif s[0] in second:
                for i in range(1, len(s)):
                    if s[i] not in second:
                        confirm = False
                        break
                if confirm:
                    ans.append(s)
            else:
                for i in range(1, len(s)):
                    if s[i] not in third:
                        confirm = False
                        break
                if confirm:
                    ans.append(s)
        return ans
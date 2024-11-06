class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        ans = 0
        for char in s:
            if char == " ":
                if ans == 0:     
                    continue
                count = 0
            else:
                count += 1
                ans = count
        return ans  
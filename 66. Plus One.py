class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        s = ""
        for i in digits:
            s += str(i)
        s = int(s) + 1
        s = str(s)
        for i in range(len(s)):
            ans.append(int(s[i]))
        return ans
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic =  collections.defaultdict(int)
        l = 0
        n = len(s)
        res = 0

        for r in range(n):
            dic[s[r]] += 1
            while dic[s[r]] > 1:
                dic[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
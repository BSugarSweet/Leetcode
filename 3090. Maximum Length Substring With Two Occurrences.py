class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        count = Counter()
        ans = 0
        l = 0

        for r, char in enumerate(s):
            count[char] += 1
            while count[char] == 3:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans








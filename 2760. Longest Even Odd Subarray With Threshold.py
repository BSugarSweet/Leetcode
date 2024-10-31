class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        ans = 0

        for l in range(n):
            if nums[l] > threshold:
                continue
            if nums[l] % 2 != 0:
                continue
            
            length = 1
            for r in range(l + 1, n):
                if nums[r] > threshold:
                    l = r - 1
                    break
                if nums[r] % 2 == nums[r - 1] % 2:
                    l = r - 1
                    break
                length += 1
            ans = max(ans, length)
        return ans
                
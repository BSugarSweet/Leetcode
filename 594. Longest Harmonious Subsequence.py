class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        ans = 0

        for r in range(n):
            while nums[r] - nums[l] > 1:
                l += 1
            if nums[r] - nums[l] == 1:
                ans = max(ans, r - l + 1)
            r += 1
        return ans
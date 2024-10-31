class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        minimum = float('inf')

        for i in range(n-k+1):
            minimum = min(minimum, nums[i + k - 1] - nums[i])
        return minimum

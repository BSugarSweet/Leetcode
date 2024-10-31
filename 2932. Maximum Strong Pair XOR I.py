class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        maximum = 0
        n = len(nums)
        nums.sort()

        if n == 1:
            return 0

        for l in range(n):
            for r in range(l, n):
                if (nums[r] - nums[l]) > min(nums[r], nums[l]):
                    break
                maximum = max(maximum, (nums[r] ^ nums[l]))
        return maximum 
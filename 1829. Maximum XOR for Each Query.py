class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        all_xor = nums[0]
        n = len(nums)
        max_num = (1 << maximumBit) - 1
        ans = []

        for i in range(1, n):
            all_xor ^= nums[i]

        for i in range(n):
            ans.append(max_num ^ all_xor)
            all_xor ^= nums[n - 1 - i]

        return ans

        
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        n = len(nums)

        for left in range(n):
            num = 0  
            for right in range(left, n):
                num |= nums[right]

                if num >= k:
                    ans = min(ans, right - left + 1)
                    break
        
        return ans if ans != float('inf') else -1
        
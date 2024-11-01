class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        minimum = float('inf')
        ans = 0

        for i in range(n - 2):
            t = target - nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                num = nums[l] + nums[r]
                if (abs(num - t) < minimum):
                    minimum = abs(num - t)
                    ans = num + nums[i]
                if num > t:
                    r -= 1
                elif num < t:
                    l += 1
                elif num == t:
                    return target
        return ans

        
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        maxima = float('-inf')
        s = 0
        tmp = 0
        for i in range(k):
            s += nums[i]
            tmp = s / k
        maxima = max(maxima, tmp)
        for i in range(k,n):
            s = s - nums[i-k] + nums[i]
            tmp = s / k
            maxima = max(maxima, tmp)
        return maxima
            

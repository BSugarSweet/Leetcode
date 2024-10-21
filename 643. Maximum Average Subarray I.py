class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        maxima = float('-inf')
        for i in range(n - k + 1):
            s = 0
            for j in range(i,i+k):
                s += nums[j]
            s = s / k
            maxima = max(maxima, s)
        return maxima

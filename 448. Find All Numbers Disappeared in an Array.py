class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set()

        for i in range(1, n+1):
            s.add(i)

        for num in nums:
            if num in s:
                s.remove(num)

        return list(s)
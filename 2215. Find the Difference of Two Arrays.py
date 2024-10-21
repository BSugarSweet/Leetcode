class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        ans.append(list(set_nums1 - set_nums2))
        ans.append(list(set_nums2 - set_nums1))
        return ans
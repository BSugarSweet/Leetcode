class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = collections.Counter(nums1)
        dic2 = collections.Counter(nums2)
        res = []
        
        for key in dic1:
            if key in dic2:
                for i in range(min(dic1[key], dic2[key])):
                    res.append(key)

        return res
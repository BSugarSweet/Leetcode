class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        seen = set()
        for i in arr:
            dic[i] = dic.get(i, 0) + 1
        for i in dic:
            if dic[i] in seen:
                return False
            seen.add(dic[i])
        return True
        



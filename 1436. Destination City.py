class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dic = dict()

        for start, end in paths:
            dic[start] = end
        for start in dic:
            if dic[start] not in dic:
                return dic[start]
        
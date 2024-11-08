class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dic = collections.Counter(deck)
        count = dic.values()
        gcd = math.gcd(*count)
        return gcd != 1
        
        
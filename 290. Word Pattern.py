class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        dic = dict()
        used = set()

        if len(pattern) != len(words):
            return False

        for i in range(len(words)):
            if words[i] not in dic:
                if pattern[i] in used:
                    return False
                used.add(pattern[i])
                dic[words[i]] = pattern[i]
                continue
            if pattern[i] != dic[words[i]]:
                return False
        
        return True

        
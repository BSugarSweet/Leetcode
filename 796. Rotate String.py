class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        start = s.find(goal[0])
        n = len(s)
        if n != len(goal):
            return False
        if start == -1:
            return False
        
        for i in range(start, n):
            if s[i] != goal[i - start]:
                return False
        for i in range(start):
            if s[i] != goal[start + i + 1]:
                return False
        return True
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        colors.append(colors[0])
        colors.append(colors[1])
        ans = 0

        for i in range(n):
            if colors[i] == 0 and colors[i+1] == 1 and colors[i+2] == 0 or colors[i] == 1 and colors[i+1] == 0 and colors[i+2] == 1:
                ans += 1
            
        return ans




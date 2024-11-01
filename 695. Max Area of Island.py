class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m = len(grid)
        n = len(grid[0])
        stk = []
        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in seen:
                    area = 0
                    stk.append((i, j))
                    seen.add((i, j))
                    
                    while stk:
                        x, y = stk.pop()
                        area += 1
                        
                        for delta_x, delta_y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                            new_x = x + delta_x
                            new_y = y + delta_y
                            if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] and (new_x, new_y) not in seen:
                                stk.append((new_x, new_y))
                                seen.add((new_x, new_y))
                    max_area = max(max_area, area)
        return max_area
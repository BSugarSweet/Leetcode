class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        m = len(grid)
        n = len(grid[0])
        stk = []
        island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in seen:
                    island += 1
                    seen.add((i, j))
                    stk.append((i, j))

                    while stk:
                        x, y = stk.pop()
                        for delta_x, delta_y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                            new_x = x + delta_x
                            new_y = y + delta_y
                            if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == '1' and (new_x, new_y) not in seen:
                                stk.append((new_x, new_y))
                                seen.add((new_x, new_y))
        return island
                    

        
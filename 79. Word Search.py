class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = set()
        count = {}

        def bfs(x, y, k):
            if k == len(word):
                return True
            if not (0 <= x < m) or not (0 <= y < n) or (x, y) in visited or board[x][y] != word[k]:
                return False

            visited.add((x, y))
            res = bfs(x - 1, y, k + 1) or bfs(x + 1, y, k + 1) or bfs(x, y + 1, k + 1) or bfs(x , y - 1, k + 1)
            visited.remove((x, y))
            return res

        for c in word:
            count[c] = 1 + count.get(c, 0)
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        for x in range(m):
            for y in range(n):
                if bfs(x, y, 0):
                    return True
        return False

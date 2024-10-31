class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0
        n = len(blocks)
        for i in range(k):
            if blocks[i] == 'W':
                white += 1
        minimum = white

        for i in range(k, n):
            if blocks[i-k] == 'W':
                white -= 1
            if blocks[i] == 'W':
                white += 1
            minimum = min(minimum, white)
        return minimum        
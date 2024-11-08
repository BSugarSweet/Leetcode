class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        _count = 0
        position = 0
        for i in moves:
            if i == 'R':
                position += 1
            elif i == 'L':
                position -= 1
            else:
                _count += 1
        if position >= 0:
            return position + _count
        else:
            return -position + _count
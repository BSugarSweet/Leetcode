# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            res = guess((left + right) / 2)
            if res == -1:
                right = (left + right) / 2
            elif res == 1:
                left = (left + right) / 2
            else:
                return int((left + right) / 2)
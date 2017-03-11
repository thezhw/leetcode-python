# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


def guess(num: int) -> int:
    return num == 3


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2

            if guess(mid) == 0:
                return mid
            elif guess(mid) > 0:
                left = mid + 1
            else:
                right = mid - 1

        return -1

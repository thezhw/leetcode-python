# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


def guess(num: int) -> int:
    if num == 3:
        return 0
    elif num < 3:
        return 1
    else:
        return -1


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


class Solution1:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2
            if guess(mid) > 0:
                left = mid + 1
            else:
                right = mid

        return left


solution = Solution1()
print(solution.guessNumber(100000))

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                # 如果 mid 为第一个平方大于 x 的整数, mid - 1 即为最后一个平方不大于 x 的整数
                # 所以最后返回应返回 right
                right = mid - 1

        return right


class Solution1:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x // 2 + 1
        while left < right:
            # mid 的含义: 第一个平方小于等于 x 的数
            mid = (left + right + 1) // 2

            if mid * mid > x:
                right = mid - 1
            else:
                left = mid

        return left


solution = Solution1()
print(solution.mySqrt(0))
print(solution.mySqrt(8))
print(solution.mySqrt(9))

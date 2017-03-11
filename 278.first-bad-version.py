# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


def isBadVersion(version):
    return version >= 1


# 超时
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(1, n + 1):
            if isBadVersion(i):
                return i


# 二分查找法
class Solution1:
    def firstBadVersion(self, n):
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2  # java c++ 等语言防止溢出
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid

        return right


solution = Solution1()
print(solution.firstBadVersion(100))

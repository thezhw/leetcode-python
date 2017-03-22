# 顺序查找
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si, ti = 0, 0
        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si += 1
            ti += 1

            if si == len(s):
                return True

            if ti == len(t):
                return False

        return False if s else True


solution = Solution()
print(solution.isSubsequence('', 'aafafaf'))
print(solution.isSubsequence('abc', ''))
print(solution.isSubsequence('abc', 'abc'))
print(solution.isSubsequence('abc', 'ahbgdc'))
print(solution.isSubsequence('axc', 'ahbgdc'))

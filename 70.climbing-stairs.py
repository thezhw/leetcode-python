class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0, 1, 2]
        for i in range(3, n + 1):
            res.append(res[i - 1] + res[i - 2])

        return res[n]


solution = Solution()
print(solution.climbStairs(3))

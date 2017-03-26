# 动态规划
import collections


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n):
                if i - j * j < 0:
                    break
                dp[i] = min(dp[i], dp[i - j * j] + 1)

        return dp[-1]


# BFS
class Solution1:
    def numSquares(self, n: int) -> int:
        queue = collections.deque()
        queue.append((n, 0))
        visited = set()

        while queue:
            value, depth = queue.popleft()
            for i in range(1, int(value ** 0.5) + 1):
                remainder_value = value - i * i
                if remainder_value == 0:
                    return depth + 1
                if remainder_value not in visited:
                    queue.append((remainder_value, depth + 1))
                    visited.add(remainder_value)


solution = Solution1()
print(solution.numSquares(12))

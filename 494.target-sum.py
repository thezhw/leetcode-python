from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def dfs(i, total, d={}):
            if i < len(nums) and (i, total) not in d:
                d[(i, total)] = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])

            return d.get((i, total), int(total == S))

        return dfs(0, 0)


solution = Solution()
print(solution.findTargetSumWays([1, 1, 1, 1, 1], 3))

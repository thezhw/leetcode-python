class Solution:
    def arrangeCoins(self, n: int) -> int:
        step = 1

        while n >= step:
            n -= step
            step += 1

        return step - 1


solution = Solution()
print(solution.arrangeCoins(5))
print(solution.arrangeCoins(8))

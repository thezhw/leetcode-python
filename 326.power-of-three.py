class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        power = 0
        i = 0

        while power < n:
            power = pow(3, i)
            i += 1

            if power == n:
                return True

        return False


solution = Solution()
print(solution.isPowerOfThree(10))

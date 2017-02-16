class Solution:
    def reverse(self, x: int) -> int:
        abs_x = abs(x)
        reverse_x = 0

        while abs_x != 0:
            remainder = abs_x % 10
            reverse_x = reverse_x * 10 + remainder
            abs_x //= 10

        reverse_x = 0 if reverse_x > 2 ** 31 else reverse_x

        return reverse_x if x > 0 else -reverse_x


solution = Solution()
print(solution.reverse(-133234))

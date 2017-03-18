# 暴力
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        for i in range(n):
            ans *= x

        return ans


# 快速幂 递归
class Solution1:
    def myPow(self, x: float, n: int) -> float:
        def fastPow(x_num, n_num):
            if n_num == 0:
                return 1.0

            half = fastPow(x_num, n_num // 2)
            if n_num % 2 == 0:  # 偶数
                return half * half
            else:
                return half * half * x_num

        if n < 0:
            x = 1 / x
            n = -n

        return fastPow(x, n)


# 快速幂 迭代
class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        product = x
        while n > 0:
            if n % 2 == 1:
                ans = ans * product
            product *= product

            n //= 2

        return ans


solution = Solution2()
# print(solution.myPow(2, 4))
print(solution.myPow(8.84327, -5))

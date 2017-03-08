# 函数调用
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


# 十进制转二进制
class Solution1:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            res = n % 2
            if res == 1:
                count += 1
            n //= 2

        return count

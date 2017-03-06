import math


# 暴力
class Solution:
    def countPrimes(self, n: int) -> int:

        def isPrime(num):
            if num < 2:
                return False

            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False

            return True

        count = 0
        for j in range(1, n):
            if isPrime(j):
                count += 1

        return count


# 暴力
class Solution1:
    def countPrimes(self, n: int) -> int:
        count = 0

        for i in range(2, n):
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                count += 1

        return count


# 厄拉多塞筛法
class Solution2:
    def countPrimes(self, n: int) -> int:
        is_primes = [1] * n
        count = 0

        for i in range(2, n):
            if is_primes[i] == 1:
                count += 1

            j = i
            while i * j < n:
                is_primes[i * j] = 0
                j += 1

        return count


class Solution3:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_primes = [1] * n
        is_primes[0] = is_primes[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if is_primes[i]:
                is_primes[i * i:n:i] = [0] * len(is_primes[i * i:n:i])

        return sum(is_primes)


solution = Solution2()
print(solution.countPrimes(10))

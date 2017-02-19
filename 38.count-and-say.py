class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        num_count = 0
        num = ''
        res = ''

        for ch in self.countAndSay(n - 1):
            if ch != num:
                if num_count > 0:
                    res += str(num_count) + num
                num_count = 1
                num = ch
            else:
                num_count += 1

        res += str(num_count) + num

        return res


solution = Solution()
print(solution.countAndSay(1))
print(solution.countAndSay(2))
print(solution.countAndSay(3))
print(solution.countAndSay(4))
print(solution.countAndSay(5))
print(solution.countAndSay(6))

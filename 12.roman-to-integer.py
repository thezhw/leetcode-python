class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0

        for idx in range(len(s) - 1):
            # 左字符值 < 右字符值
            if roman_dict[s[idx]] < roman_dict[s[idx + 1]]:
                total -= roman_dict[s[idx]]
            else:
                total += roman_dict[s[idx]]

        return total + roman_dict[s[-1]]


solution = Solution()
print(solution.romanToInt('MCMXCIV'))

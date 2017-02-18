import re


class Solution:
    def myAtoi(self, str: str) -> int:
        re_str = r'[-|+]?\d+'
        res = re.match(re_str, str.strip(' '))
        try:
            res = int(res[0])
        except TypeError:
            return 0

        return max(min(res, 2 ** 31 - 1), (-2) ** 31)

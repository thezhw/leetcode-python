from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(1, len(digits) + 1):
            if digits[-i] != 9:
                digits[-i] += 1
                return digits
            digits[-i] = 0

        digits.insert(0, 1)
        return digits


solution = Solution()
print(solution.plusOne([1, 2, 3]))
print(solution.plusOne([1, 2, 9]))
print(solution.plusOne([9, 9, 9]))

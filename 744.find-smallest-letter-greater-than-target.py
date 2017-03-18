from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        # 寻找第一个比 target 大的字母
        while left < right:
            mid = (left + right) // 2
            if letters[mid] == target and letters[mid + 1] > target:
                return letters[mid + 1]
            elif letters[mid] <= target:
                left += 1
            else:
                right = mid

        if letters[right] > target:
            return letters[right]

        return letters[0]


solution = Solution()
print(solution.nextGreatestLetter(["c", "f", "j"], 'g'))
print(solution.nextGreatestLetter(["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], 'e'))

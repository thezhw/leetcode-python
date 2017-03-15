from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        ans = [[1]]

        for i in range(1, numRows):
            arr = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    arr.append(1)
                else:
                    arr.append(ans[i - 1][j - 1] + ans[i - 1][j])
            ans.append(arr)

        return ans


solution = Solution()
print(solution.generate(4))

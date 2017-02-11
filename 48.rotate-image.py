from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 转置
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 反转
        for i in range(len(matrix)):
            matrix[i].reverse()

        print(matrix)


solution = Solution()
solution.rotate([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

solution.rotate([
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
])

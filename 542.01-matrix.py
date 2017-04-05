from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        ans = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    ans[i][j] = 0
                    queue.append((i, j))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            curr = queue.popleft()
            for k in range(len(directions)):
                i_new = curr[0] + directions[k][0]
                j_new = curr[1] + directions[k][1]
                if 0 <= i_new < rows and 0 <= j_new < cols:
                    if ans[i_new][j_new] > ans[curr[0]][curr[1]] + 1:
                        ans[i_new][j_new] = ans[curr[0]][curr[1]] + 1
                        queue.append((i_new, j_new))

        return ans

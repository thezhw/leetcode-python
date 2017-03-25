from collections import deque
from typing import List


# DFS
class Solution:
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if not marked[i][j] and grid[i][j] == '1':
                    count += 1
                    self.__dfs(grid, i, j, m, n, marked)

        return count

    def __dfs(self, grid, i, j, m, n, marked):
        marked[i][j] = True
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                self.__dfs(grid, new_i, new_j, m, n, marked)


# BFS
class Solution1:
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if not marked[i][j] and grid[i][j] == '1':
                    count += 1
                    self.__bfs(grid, i, j, m, n, marked)

        return count

    def __bfs(self, grid, i, j, m, n, marked):
        queue = deque()
        queue.append((i, j))
        marked[i][j] = True
        while queue:
            cur_i, cur_j = queue.popleft()
            for direction in self.directions:
                new_i = cur_i + direction[0]
                new_j = cur_j + direction[1]
                if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                    queue.append((new_i, new_j))
                    marked[new_i][new_j] = True


if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '1']]
    solution = Solution1()
    result = solution.numIslands(grid)
    print(result)

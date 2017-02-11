from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 检查行
        for i in range(9):
            dot_len = board[i].count('.')
            dig_len = len(set(board[i])) - 1
            if dig_len + dot_len < 9:
                return False

        # 检查列
        for j in range(9):
            cols = []
            for i in range(9):
                cols.append(board[i][j])

            dot_len = cols.count('.')
            dig_len = len(set(cols)) - 1
            if dig_len + dot_len < 9:
                return False

        # 检查块
        for k in range(3):
            for j in range(3):
                blocks = []
                for i in range(3):
                    blocks += board[k * 3 + i][j * 3:j * 3 + 3]

                # print(blocks)

                dot_len = blocks.count('.')
                dig_len = len(set(blocks)) - 1
                if dig_len + dot_len < 9:
                    return False

        return True


solution = Solution()
print(solution.isValidSudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))

print(solution.isValidSudoku([
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))

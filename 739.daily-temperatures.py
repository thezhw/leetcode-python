from typing import List


# 暴力
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        nxt = [float('inf')] * 102
        ans = [0] * len(T)
        for i in range(len(T) - 1, -1, -1):
            warmer_index = min(nxt[t] for t in range(T[i] + 1, 102))
            if warmer_index < float('inf'):
                ans[i] = warmer_index - i
            nxt[T[i]] = i
        return ans


# 栈 从后向前
class Solution1:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = []
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)

        return ans


# 栈 从前向后
class Solution2:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = []
        for i in range(0, len(T)):
            while stack and T[i] > T[stack[-1]]:
                top = stack.pop()
                ans[top] = i - top
            stack.append(i)

        return ans


solution = Solution2()
print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

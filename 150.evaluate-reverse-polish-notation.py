from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                stack.append(-stack.pop() + stack.pop())
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                num = stack.pop()
                stack.append(int(stack.pop() / num))
            else:
                stack.append(int(token))

        return stack.pop()


solution = Solution()
print(solution.evalRPN(["2", "1", "+", "3", "*"]))
print(solution.evalRPN(["4", "13", "5", "/", "+"]))
print(solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ']':
                rep_str = ''
                while stack[-1] != '[':
                    rep_str = stack.pop() + rep_str

                stack.pop()  # pop '['

                rep_count = ''
                while len(stack) > 0 and '0' <= stack[-1] <= '9':
                    rep_count = stack.pop() + rep_count

                stack.append(rep_str * int(rep_count))
            else:
                stack.append(char)

        return ''.join(stack)


solution = Solution()
print(solution.decodeString('3[a]2[bc]'))
print(solution.decodeString('3[a2[c]]'))
print(solution.decodeString('2[abc]3[cd]ef'))
print(solution.decodeString('10[l]'))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from public.TreeNode import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        ans = []
        stack = [(root, WHITE)]

        while stack:
            node, color = stack.pop()
            if node is None:
                continue
            if color == WHITE:
                stack.append((node.right, WHITE))
                stack.append((node.left, WHITE))
                stack.append((node, GRAY))
            else:
                ans.append(node.val)

        return ans


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
solution = Solution()
print(solution.preorderTraversal(root))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from public.TreeNode import TreeNode


# 递归
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def helper(left, right):
            # 左右节点同时为空
            if left is None and right is None:
                return True

            # 左右节点不同时为空
            if not (left and right):
                return False

            # 左右节点值不相等
            if left.val != right.val:
                return False

            if not helper(left.left, right.right):
                return False

            if not helper(left.right, right.left):
                return False

            return True

        return helper(root.left, root.right)

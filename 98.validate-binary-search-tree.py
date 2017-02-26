# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from public.TreeNode import TreeNode


# 递归
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if node is None:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            # 验证左子树
            if not helper(node.left, lower, val):
                return False

            # 验证右子树
            if not helper(node.right, val, upper):
                return False

            return True

        return helper(root)

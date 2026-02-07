# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        def dfs(node):
            # 如果節點是空的，深度 = 0
            if not node:
                return 0
            # 遞迴計算左右子樹深度
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            # 當前節點深度 = 1 + 左右子樹最大值
            return 1 + max(left_depth, right_depth)

        return dfs(root)

# Runtime: 1 ms Beats 38.07 %
# Memory: 20.44 MB Beats 14.76 %

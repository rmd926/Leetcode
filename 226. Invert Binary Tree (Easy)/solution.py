# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        temp = root.left # 先暫時存原本的left node
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)

        return root

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.50 MB Beats 13.46 %

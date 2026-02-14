# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            
            if node.val > val:
                return dfs(node.left)
            if node.val < val:
                return dfs(node.right)
            else:
                return node

        return dfs(root) 

# Runtime: 0 ms Beats 100.00 %
# Memory: 21.02 MB Beats 28.15 %

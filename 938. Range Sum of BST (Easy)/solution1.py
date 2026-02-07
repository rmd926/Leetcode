# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = []
        def dfs(node):
            if not node:
                return

            if low <= node.val <= high:
                ans.append(node.val)
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return sum(ans)

# Runtime: 12 ms Beats 33.09 %
# Memory: 26.07 MB Beats 48.95 %

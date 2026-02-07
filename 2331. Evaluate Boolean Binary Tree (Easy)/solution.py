# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node.left and not node.right:
                return node.val == 1
                
            # 處理OR nodes
            if node.val == 2:
                return dfs(node.left) or dfs(node.right)

            # 處理AND nodes
            elif node.val == 3:
                return dfs(node.left) and dfs(node.right)
            
        return dfs(root)

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.67 MB Beats 24.78 %

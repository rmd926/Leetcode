# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_level = 1
        ans = 0

        def dfs(node, level):
            nonlocal max_level
            nonlocal ans

            if not node:
                return 

            if level == max_level:
                ans += node.val

            elif level > max_level:
                max_level = level
                ans = node.val
            
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        
        dfs(root, 1)
        return ans

# Runtime: 11 ms Beats 74.17 %
# Memory: 22.64 MB Beats 5.30 %

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, cur_max):
            count = 0
            if not node:
                return 0

            # 若當前值 >= 路徑最大值，代表路徑上沒有比它更大的值 -> good node
            if node.val >= cur_max:
                count += 1
            
            # update cur_max
            cur_max = max(node.val, cur_max)
            count += dfs(node.left, cur_max)
            count += dfs(node.right, cur_max)

            return count
        
        return dfs(root, root.val)

# Runtime: 134 ms Beats 48.51 %
# Memory: 31.87 MB Beats 65.90 %

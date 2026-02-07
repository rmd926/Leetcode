# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 1
        count += self.countNodes(root.left)
        count += self.countNodes(root.right)
    
        return count

# Runtime: 3 ms Beats 50.78 %
# Memory: 23.89 MB Beats 25.57 %

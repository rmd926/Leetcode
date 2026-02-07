# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        
        tree = TreeNode(root1.val + root2.val)
        tree.left = self.mergeTrees(root1.left, root2.left)
        tree.right = self.mergeTrees(root1.right, root2.right)
    
        return tree

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.79 MB Beats 9.12 %

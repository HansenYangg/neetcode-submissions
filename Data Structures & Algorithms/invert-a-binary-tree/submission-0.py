# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # if root is empty, return 
        # invert left and right children 
        # recursively call func on children, which will invert the lower layers
        def dfs(tree):
            if not tree:
                return 
            tree.left, tree.right = tree.right, tree.left
            dfs(tree.left)
            dfs(tree.right)
        dfs(root)
        return root


        
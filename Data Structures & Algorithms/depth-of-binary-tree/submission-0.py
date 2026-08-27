# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(tree, height):
            if not tree:
                return height
            return max(dfs(tree.left, height + 1), dfs(tree.right, height + 1))
        
        return dfs(root, 0)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(tree, lower, upper):
            if not tree:
                return True
            valid = lower < tree.val < upper
            return valid and dfs(tree.left, lower, tree.val) and dfs(tree.right, tree.val, upper)

        return dfs(root, float("-inf"), float("inf"))


            
    
            
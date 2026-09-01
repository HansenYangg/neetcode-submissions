# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # helper function to get height of a tree
        # at a given node, check if heights differ by >1 and return false if so
        # else, recursive call on both left and right children
        def getHeight(tree, height):
            if not tree:
                return height
            
            return max(getHeight(tree.left, height + 1), getHeight(tree.right, height + 1))
            

        if not root:
            return True
        if abs(getHeight(root.left, 0) - getHeight(root.right, 0)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
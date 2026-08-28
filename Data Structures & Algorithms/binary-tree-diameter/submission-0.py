# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = []

        def getHeight(tree, height):
            if not tree:
                return height
            return max(getHeight(tree.left, height + 1), getHeight(tree.right, height + 1))

        def dfs(tree):
            if not tree:
                
                return
            res.append(getHeight(tree.left, 0) + getHeight(tree.right, 0))
            dfs(tree.left)
            dfs(tree.right)
        print(res)
        dfs(root)
        print(res)
        return max(res)
        


        
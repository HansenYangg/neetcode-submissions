# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def preOrder(tree):
            if not tree:
                return 

            res.append(tree.val)
            preOrder(tree.left)
            preOrder(tree.right)

        preOrder(root)
        return res
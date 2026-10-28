# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inOrder(tree):
            if not tree:
                return

            inOrder(tree.left)
            res.append(tree.val)
            inOrder(tree.right)

        inOrder(root)
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # helper dfs function, with another arg that maintains the curr max value that we've encountered on the path to our current node. if curr node.val > max value, then we found a good node. continue to traverse down children with updated max value
        if not root:
            return 0

        res = 1
        def dfs(tree, curr_max):
            if not tree:
                return 

            nonlocal res
            if tree.val >= curr_max:
                res += 1
                dfs(tree.left, tree.val)
                dfs(tree.right, tree.val)
            else:
                dfs(tree.left, curr_max)
                dfs(tree.right, curr_max)


        dfs(root.left, root.val)
        dfs(root.right, root.val)
        return res
            

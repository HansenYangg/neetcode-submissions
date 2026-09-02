# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''traverse via dfs through root with helper function , mapping each child:parent in a hashmap. after traversal, we should have a fully mapped out structure, and we can iteratively append all the parents of p (and p itself) to a set. then, iteratively climb up q's parents and return as soon as we find that the current parent of q (or q itself) is in our set, because this will be the LCA.
        '''
        m = {root: None}
        def dfs(root):
            if not root:
                return 
            nonlocal m
            if root.left:
                m[root.left] = root
            if root.right:
                m[root.right] = root
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        s, res = set(), root
        while p in m:
            s.add(p)
            p = m[p]
        
        while q in m:
            if q in s:
                return q
            q = m[q]

        return res






        







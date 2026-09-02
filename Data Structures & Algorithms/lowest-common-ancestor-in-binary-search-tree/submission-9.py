# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # traverse through root with helper function , mapping each parent:child in a hashmap
        # after traversal, we should have a fully mapped out map, and we can iteratively append all the parents of both p and q to some list, and just return the min
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
        s.add(p)
      
    
        while p in m:
            s.add(m[p])
            p = m[p]
        
        while q in m:
            if q in s:
                return q
            q = m[q]

        return res






        







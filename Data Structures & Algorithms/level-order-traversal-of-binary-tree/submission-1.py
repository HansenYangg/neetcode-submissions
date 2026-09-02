# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''helper dfs function that keeps track of level, and adds it to a map
        that maps level: array of all values at that level

        return just the value arrays of our map

        bfs starting from root, which will be level 0
        will just be 0 mapped to [root.val]
        bfs with level + 1, which will either create new mapping or update mapping with
        level + 1: mapped to new array
        '''
        m = {}
        def bfs(tree, level):
            nonlocal m

            if not tree:
                return 

            if level not in m:
                m[level] = [tree.val]
            else:
                m[level].append(tree.val)

            bfs(tree.left, level + 1)
            bfs(tree.right, level + 1)



        bfs(root, 0)
        return list(m.values())
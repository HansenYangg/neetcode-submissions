# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # level order traversal, but only return the last element of each level
        queue = deque()
        queue.append(root)

        res = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)



            res.append(level[-1])



        return res
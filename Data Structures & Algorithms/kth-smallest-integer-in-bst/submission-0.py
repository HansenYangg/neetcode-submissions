# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    import heapq
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        heap = []
        def dfs(tree):
            if not tree:
                return 
            heapq.heappush(heap, -tree.val)
            if len(heap) > k:
                heapq.heappop(heap)
            dfs(tree.left)
            dfs(tree.right)
        dfs(root)
        return -heap[0]
        
            

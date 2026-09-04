# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = None
        flattened = []
        for sub_list in lists:
            while sub_list:
                flattened.append(sub_list.val)
                sub_list = sub_list.next
        flattened.sort()
        for num in flattened[::-1]:

            res = ListNode(num, res)
        return res


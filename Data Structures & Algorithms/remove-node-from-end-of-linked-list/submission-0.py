# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = dummy = curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        # head = [1,2,3,4,5,6,7] ; n = 2
        # length = 7
        # iters = 4
        iters = length - n - 1
        if iters == -1:
            return head.next
     

        while dummy and iters:
            dummy = dummy.next
            iters -= 1

        if dummy and dummy.next:
            dummy.next = dummy.next.next

        return res



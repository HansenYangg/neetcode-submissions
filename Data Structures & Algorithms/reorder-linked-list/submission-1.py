# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        res = beginning = slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        dummy = beginning
        while beginning and beginning.next != slow:
            beginning = beginning.next
        if beginning:
            beginning.next = None

       
        # reverse slow 
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        last = None
        while prev and dummy:
            temp1 = prev.next
            temp2 = dummy.next
            prev.next = dummy.next
            dummy.next = prev
            last = prev
            prev = temp1
            dummy = temp2

        if prev:
            last.next = prev



        

            




        

            
       

      
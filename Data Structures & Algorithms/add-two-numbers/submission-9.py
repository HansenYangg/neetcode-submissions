# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # iterate through l1 and just add all the values of l2 to each value
        # if l1.val + l2.val > 10, we need to add a new node in front of l1 while preserving the rest
        

        head = curr = l1
        carry, prev = False, None
        while curr and l2: 
            val = curr.val + l2.val
            if carry: 
                val += 1

            if val >= 10:
                carry = True
                curr.val = val % 10
            else:
                curr.val = val
                carry = False
            
            prev = curr
            curr = curr.next
            l2 = l2.next

        while curr:
            val = curr.val
            if carry:
                val += 1
            if val >= 10:
                curr.val = val % 10
            else:
                carry = False
                curr.val = val
            prev = curr
            curr = curr.next

        while l2:
            val = l2.val
            if carry:
                val += 1
            if val >= 10:
                prev.next = ListNode(val % 10)
            else:
                prev.next = ListNode(val)
                carry = False
            l2 = l2.next
            prev = prev.next
                


        if carry:
            prev.next = ListNode(1)

        return head

# l1 = [1, 7, 3], l2 = [4,5,6] --> (5, 1, 2, 9)
# 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        
        curr1 = slow =  head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        reverse = self.reverse(head2)
        
        

        while reverse:
            t1, t2 = curr1.next, reverse.next
            curr1.next = reverse
            reverse.next = t1

            curr1, reverse = t1, t2

            

    def reverse(self, curr):
        prev = None
        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
        return prev
            



        
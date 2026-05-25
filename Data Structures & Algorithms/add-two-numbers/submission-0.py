# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        res = dummy = ListNode(0)
        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            dig = val1 + val2 + carry
            curr_sum = (val1 + val2 + carry) % 10
            carry = (dig) // 10

            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next
            res.next = ListNode(curr_sum)
            res = res.next
        return dummy.next



        
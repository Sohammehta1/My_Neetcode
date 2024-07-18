# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            a = l1.val +l2.val
            if carry:
                a +=1
                carry = 0
            if a>=10:
                carry = 1
                a -=10
            curr.next = ListNode(a)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            a = l1.val
            if carry:
                a +=1
                carry = 0
            if a>=10:
                a -=10
                carry = 1
            curr.next = ListNode(a)
            curr = curr.next
            l1 = l1.next
        while l2:
            a = l2.val
            if carry:
                a +=1
                carry = 0
            if a>=10:
                a -=10
                carry = 1
            curr.next = ListNode(a)
            curr = curr.next
            l2 = l2.next
        if carry:
            curr.next= ListNode(1)
        return dummy.next
            

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # now the next of slow is the second part of the list

        # Reversing the list
        second = slow.next
        prev =slow.next = None # the list has been split
        while second:
            temp = second.next
            second.next= prev
            prev = second
            second = temp
        # merging the two halves
        second = prev
        first = head
        while first and second:
            temp = first.next
            first.next = second
            temp2 = second.next
            second.next = temp
            second = temp2
            first = first.next.next
         



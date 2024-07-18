from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        left = head
        right= head
        while n>0 and right:
            n-=1
            right = right.next
        while right:
            prev = left
            left =left.next
            right = right.next
        if prev ==None:
            head = left.next
            
        else:
            prev.next = left.next
        del left
        return head
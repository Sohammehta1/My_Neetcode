# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next == None:
            return head
        stack = []
        prev = head
        head = head.next
        stack.append(prev)
        while head.next:
            prev = head
            head = head.next
            stack.append(prev)
        new_head = head
        while stack:
            head.next = stack.pop()
            head = head.next
        head.next = None
        return new_head
        
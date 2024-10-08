from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        new_head =head
    

        while list1 and list2:
            if list1.val > list2.val:
                head.next = ListNode(val = list2.val)
                list2 = list2.next
            else:
                head.next = ListNode(val =list1.val)
                list1 = list1.next
            head = head.next
        if list1:
            head.next= list1
        elif list2:
            head.next = list2
        return new_head.next
            
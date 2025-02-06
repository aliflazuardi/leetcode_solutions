# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head is not None and head.val == val:
            head = head.next

        curr = head

        while curr is not None:
            while curr.next is not None and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next

        return head

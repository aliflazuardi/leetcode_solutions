# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        curr_odd = head
        even_head = head.next
        curr_even = even_head
        curr = head.next.next

        is_odd = True
        while curr:
            if is_odd:
                curr_odd.next = curr
                curr_odd = curr
                is_odd = False
            else:
                curr_even.next = curr
                curr_even = curr
                is_odd = True
            curr = curr.next

        curr_even.next = None
        curr_odd.next = even_head
        return head

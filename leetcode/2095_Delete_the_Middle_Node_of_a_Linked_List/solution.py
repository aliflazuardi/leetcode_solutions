# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        fp = head
        sp = head

        while fp is not None:
            fp = fp.next
            if fp is None or fp.next is None:
                break
            fp = fp.next
            if fp.next is not None:
                sp = sp.next

        np = sp.next
        if np is not None:
            sp.next = np.next

        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        fp = head
        sp = head
        prev = None

        while fp is not None and fp.next is not None:
            prev = sp
            sp = sp.next
            fp = fp.next.next

        prev.next = sp.next

        return head

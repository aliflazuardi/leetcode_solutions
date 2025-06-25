# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head.next:
            return head

        curr = head

        while curr.next:
            nxt = curr.next

            val = min(curr.val, nxt.val)
            for v in range(val, 0, -1):
                if curr.val % v == 0 and nxt.val % v == 0:
                    val = v
                    break

            temp = ListNode(val)
            curr.next = temp
            temp.next = nxt
            curr = nxt

        return head

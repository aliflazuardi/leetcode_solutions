# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            after = slow.next
            slow.next = prev
            prev = slow
            slow = after

        ans = 0
        while prev:
            ans = max(ans, (prev.val + head.val))
            prev = prev.next
            head = head.next

        return ans

package solution

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return false
	}

	slow := head
	fast := head.Next

	for slow != nil || fast != nil {
		if slow == fast {
			return true
		}

		slow = slow.Next
		if fast != nil {
			fast = fast.Next
			if fast != nil {
				fast = fast.Next
			}
		}
	}

	return false
}

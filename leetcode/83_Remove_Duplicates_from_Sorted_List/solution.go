package solution

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
	curr := head
	for curr != nil {
		for curr.Next != nil && curr.Val == curr.Next.Val {
			curr.Next = curr.Next.Next
		}
		curr = curr.Next
	}

	return head
}

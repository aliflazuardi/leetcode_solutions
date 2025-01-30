package solution

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	curr1 := l1
	curr2 := l2
	c := 0
	head := ListNode{
		Val: 0,
	}
	ans := &head
	curr := ans
	for curr1 != nil || curr2 != nil {
		d := 0
		if curr1 != nil {
			d = d + curr1.Val
			curr1 = curr1.Next
		}
		if curr2 != nil {
			d = d + curr2.Val
			curr2 = curr2.Next
		}
		d = d + c
		c = 0
		if d >= 10 {
			d = d - 10
			c = 1
		}
		l := ListNode{
			Val: d,
		}
		curr.Next = &l
		curr = curr.Next
	}
	if c != 0 {
		l := ListNode{
			Val: c,
		}
		curr.Next = &l
		curr = curr.Next
	}

	return ans.Next
}

package solution

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	var head *ListNode
	var curr *ListNode
	if list1 != nil && list2 != nil {
		if list1.Val <= list2.Val {
			head = list1
			list1 = list1.Next
		} else {
			head = list2
			list2 = list2.Next
		}
	} else if list1 != nil {
		head = list1
		list1 = list1.Next
	} else if list2 != nil {
		head = list2
		list2 = list2.Next
	}
	curr = head

	for list1 != nil && list2 != nil {
		if list1.Val <= list2.Val {
			curr.Next = list1
			list1 = list1.Next
		} else {
			curr.Next = list2
			list2 = list2.Next
		}
		curr = curr.Next
	}
	for list1 != nil {
		curr.Next = list1
		list1 = list1.Next
		curr = curr.Next
	}
	for list2 != nil {
		curr.Next = list2
		list2 = list2.Next
		curr = curr.Next
	}

	return head
}

package solution

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func inorderTraversal(root *TreeNode) []int {
	ans := processNode(root)

	return ans
}

func processNode(node *TreeNode) []int {
	if node == nil {
		return []int{}
	}

	var a []int

	if node.Left != nil {
		l := processNode(node.Left)
		a = append(a, l...)
	}
	a = append(a, node.Val)
	if node.Right != nil {
		r := processNode(node.Right)
		a = append(a, r...)
	}
	return a
}

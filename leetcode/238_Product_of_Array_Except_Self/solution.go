package solution

func productExceptSelf(nums []int) []int {
	n := len(nums)
	res := make([]int, n)

	for i := range res {
		res[i] = 1
	}

	prefix := 1
	for i := range nums {
		res[i] = prefix
		prefix = prefix * nums[i]
	}

	postfix := 1
	for i := len(nums) - 1; i >= 0; i-- {
		res[i] = res[i] * postfix
		postfix = postfix * nums[i]
	}

	return res
}

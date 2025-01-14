package solution

func removeElement(nums []int, val int) int {
	l := 0
	r := len(nums) - 1
	for l <= r {
		for nums[l] == val {
			nums[l] = nums[r]
			r--
			if r < l {
				return l
			}
		}
		l++
	}

	return l
}

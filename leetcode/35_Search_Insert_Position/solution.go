package solution

func searchInsert(nums []int, target int) int {
	l := 0
	r := len(nums)
	m := l + (r-l)/2
	for l < r {
		if nums[m] == target {
			break
		} else if nums[m] > target {
			r = m
		} else {
			l = m + 1
		}
		m = l + (r-l)/2
	}

	return m
}

package solution

func alternatingSubarray(nums []int) int {
	diff := make([]int, len(nums))
	diff[0] = 1

	for i := 1; i < len(nums); i++ {
		diff[i] = nums[i] - nums[i-1]
	}

	maxLen := 0
	temp := 1
	len := 0
	for i, d := range diff {
		if i == 0 {
			continue
		}
		if temp == 1 && d == 1 {
			len = 2
		} else if temp == -1 && d == 1 {
			len++
			temp = d
		} else if temp == 1 && d == -1 && len != 0 {
			len++
			temp = d
		} else {
			len = 0
		}

		if len >= maxLen {
			maxLen = len
		}
	}

	if maxLen != 0 {
		return maxLen
	}
	return -1
}

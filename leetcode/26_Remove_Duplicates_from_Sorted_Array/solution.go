package solution

func removeDuplicates(nums []int) int {
	k := 0
	m := make(map[int]bool)
	for i := 0; i < len(nums); i++ {
		if _, ok := m[nums[i]]; !ok {
			m[nums[i]] = true
			nums[k] = nums[i]
			k++
		}
	}

	return k
}

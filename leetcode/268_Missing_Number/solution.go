package solution

func missingNumber(nums []int) int {
	m := make([]bool, len(nums)+1)

	for _, n := range nums {
		m[n] = true
	}

	for i, isPresent := range m {
		if !isPresent {
			return i
		}
	}

	return 0
}

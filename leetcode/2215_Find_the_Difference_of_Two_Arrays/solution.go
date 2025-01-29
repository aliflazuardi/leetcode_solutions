package solution

func findDifference(nums1 []int, nums2 []int) [][]int {
	var ans1 []int
	var ans2 []int
	m1 := make(map[int]bool)
	m2 := make(map[int]bool)

	for _, n := range nums1 {
		m1[n] = true
	}

	for _, n := range nums2 {
		m2[n] = true
		if !m1[n] {
			ans2 = append(ans2, n)
			m1[n] = true
		}
	}

	for _, n := range nums1 {
		if !m2[n] {
			ans1 = append(ans1, n)
			m2[n] = true
		}
	}

	var ans [][]int
	ans = append(ans, ans1)
	ans = append(ans, ans2)

	return ans
}

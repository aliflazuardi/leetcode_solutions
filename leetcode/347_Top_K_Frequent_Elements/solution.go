package solution

func topKFrequent(nums []int, k int) []int {
	m := make(map[int]int)

	for _, n := range nums {
		m[n] = m[n] + 1
	}

	freq := make([][]int, len(nums)+1)
	for i := 0; i <= len(nums); i++ {
		freq[i] = []int{}
	}
	for k, v := range m {
		freq[v] = append(freq[v], k)
	}

	var ans []int
	for i := len(freq) - 1; i >= 0; i-- {
		for _, n := range freq[i] {
			if k <= 0 {
				return ans
			}
			ans = append(ans, n)
			k--
		}
	}

	return ans
}

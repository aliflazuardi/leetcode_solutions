func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	var result []int

	for i, num := range nums {
		diff := target - num
		if _, ok := m[diff]; ok {
			result = append(result, m[diff])
			result = append(result, i)
			break
		}
		m[num] = i
	}
	return result
}

package solution

// Boyer-Moore Majority Vote Algorithm
// http://www.cs.utexas.edu/~moore/best-ideas/mjrty/
func majorityElement(nums []int) int {
	major := nums[0]
	count := 1
	for i := 1; i < len(nums); i++ {
		if count == 0 {
			major = nums[i]
			count++
		} else if major == nums[i] {
			count++
		} else {
			count--
		}
	}
	return major
}

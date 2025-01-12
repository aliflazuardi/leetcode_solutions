package solution

func merge(nums1 []int, m int, nums2 []int, n int) {
	if n == 0 {
		return
	}
	temp := make([]int, m)
	for i := 0; i < m; i++ {
		temp[i] = nums1[i]
	}
	l := 0
	r := 0
	for i := 0; i < m+n; i++ {
		if r >= n {
			nums1[i] = temp[l]
			l++
		} else if l < m && temp[l] <= nums2[r] {
			nums1[i] = temp[l]
			l++
		} else {
			nums1[i] = nums2[r]
			r++
		}
	}
}

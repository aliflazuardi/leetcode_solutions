func twoSum(nums []int, target int) []int {
    m := make(map[int]int)
    var result[]int
    var found bool
    
    for i, num := range nums {
        diff := target - num
        if _, ok := m[diff]; ok {
            if !found {
                result = append(result, m[diff])
                result = append(result, i)
                found = true
            }
        }
        m[num] = i
    }
    return result
}
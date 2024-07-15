func containsDuplicate(nums []int) bool {
    var duplicate bool
    m := make(map[int]int)
    
    for i, val := range nums {
        if _, ok := m[val]; ok {
            duplicate = true
        } else {
            m[val] = i
        }
    }
    return duplicate
}
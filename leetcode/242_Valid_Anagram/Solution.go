func isAnagram(s string, t string) bool {
    m1 := make(map[rune]int)
    m2 := make(map[rune]int)
    result := true
    
    for _, c := range s {
        if _, ok := m1[c]; ok {
            m1[c] = m1[c] + 1
        } 
        if _, ok := m1[c]; !ok {
            m1[c] = 1
        }
    }
    for _, c := range t {
        if _, ok := m2[c]; ok {
            m2[c] = m2[c] + 1
        }
        if _, ok := m2[c]; !ok {
            m2[c] = 1
        }
    }
    for _, c := range s {
        if _, ok := m2[c]; ok {
            if m1[c] != m2[c] {
                result = false
            }
        }
        if _, ok := m2[c]; !ok {
            result = false
        }
    }
    for _, c := range t {
        if _, ok := m1[c]; ok {
            if m1[c] != m2[c] {
                result = false
            }
        }
        if _, ok := m1[c]; !ok {
            result = false
        }
    }
    
    return result
}
package solution

func canConstruct(ransomNote string, magazine string) bool {
	if len(magazine) < len(ransomNote) {
		return false
	}

	m := make(map[byte]int)
	for i := 0; i < len(magazine); i++ {
		m[magazine[i]]++
	}

	for i := 0; i < len(ransomNote); i++ {
		if m[ransomNote[i]] <= 0 {
			return false
		}
		m[ransomNote[i]]--
	}

	return true
}

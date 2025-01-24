package solution

func firstUniqChar(s string) int {
	ans := -1
	m := make(map[byte]int)

	var temp int
	for i := len(s) - 1; i >= 0; i-- {
		if m[s[i]] == 0 {
			temp = i
		}

		m[s[i]]++
	}

	if m[s[temp]] == 1 {
		ans = temp
	} else if ans == -1 {
		for _, v := range m {
			if v == 1 {
				temp = len(s)
				for i := len(s) - 1; i >= 0; i-- {
					if m[s[i]] == 1 {
						temp = i
					}
				}
				return temp
			}
		}
	}

	return ans
}

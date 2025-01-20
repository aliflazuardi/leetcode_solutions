package solution

func longestCommonPrefix(strs []string) string {
	f := strs[0]
	minLen := 200
	for i := 1; i < len(strs); i++ {
		if len(strs[i]) < minLen {
			minLen = len(strs[i])
		}
		for j := 0; j < len(strs[i]); j++ {
			if j >= len(f) {
				continue
			}
			if f[j] != strs[i][j] {
				f = f[0:j]
			}
		}
	}
	if len(f) > minLen {
		f = f[0:minLen]
	}

	return f
}

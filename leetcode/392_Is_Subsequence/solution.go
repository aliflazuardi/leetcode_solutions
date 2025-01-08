package solution

func isSubsequence(s string, t string) bool {
	sp := 0
	for _, c := range t {
		if sp == len(s) {
			return true
		}
		if string(c) == string(s[sp]) {
			sp++
		}
	}

	return sp == len(s)
}

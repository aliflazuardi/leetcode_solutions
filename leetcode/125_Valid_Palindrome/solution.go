package solution

import "strings"

func isPalindrome(s string) bool {
	s = strings.ToLower(strings.ReplaceAll(s, " ", ""))

	var ps string
	for _, c := range s {
		if isAlphanumeric(c) {
			ps = ps + string(c)
		}
	}

	l := 0
	r := len(ps) - 1
	for l < r {
		if ps[l] != ps[r] {
			return false
		}
		l++
		r--
	}

	return true
}

func isAlphanumeric(c rune) bool {
	if (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9') {
		return true
	}

	return false
}

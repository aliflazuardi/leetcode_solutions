package solution

func lengthOfLastWord(s string) int {
	isFoundWord := false

	c := 0
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] == ' ' && isFoundWord {
			return c
		}
		if s[i] != ' ' {
			isFoundWord = true
			c++
		}
	}

	return c
}

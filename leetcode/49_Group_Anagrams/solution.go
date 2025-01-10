package solution

import "strconv"

func groupAnagrams(strs []string) [][]string {
	m := make(map[string][]string)
	for _, s := range strs {
		var count [26]int
		for i := 0; i < len(s); i++ {
			count[s[i]-'a']++
		}

		var key string
		for _, c := range count {
			key += "#" + strconv.Itoa(c)
		}

		m[key] = append(m[key], s)
	}

	ans := [][]string{}

	for _, v := range m {
		ans = append(ans, v)
	}

	return ans
}

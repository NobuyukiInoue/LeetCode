package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func characterReplacement(s string, k int) int {
	// 4ms
	var maxSize, start, maxWindowChar int
	m := make([]int, 52)
	for i, c := range s {
		m[c-'A']++
		if m[c-'A'] > maxWindowChar {
			maxWindowChar = m[c-'A']
		}
		if i-start+1-maxWindowChar > k {
			m[s[start]-'A']--
			start++
		}
		if i-start+1 > maxSize {
			maxSize = i - start + 1
		}
	}
	return maxSize
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	s := flds[0]
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("s = \"%s\", k = %d\n", s, k)

	timeStart := time.Now()

	result := characterReplacement(s, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

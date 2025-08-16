package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func hasSpecialSubstring(s string, k int) bool {
	// 0ms
	count := 1
	for i := 1; i < len(s); i++ {
		if s[i] != s[i-1] && count == k {
			return true
		}
		if s[i] != s[i-1] {
			count = 0
		}
		count++
	}
	return count == k
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	s := flds[0]
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("s = \"%s\", k = %d\n", s, k)

	timeStart := time.Now()

	result := hasSpecialSubstring(s, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

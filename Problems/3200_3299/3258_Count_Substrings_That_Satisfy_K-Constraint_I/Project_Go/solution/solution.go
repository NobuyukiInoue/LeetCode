package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func countKConstraintSubstrings(s string, k int) int {
	// 0ms
	ans, n := 0, len(s)
	for i := 0; i < n; i++ {
		count0, count1 := 0, 0
		for j := i; j < n; j++ {
			if s[j] == '0' {
				count0++
			} else {
				count1++
			}
			if count0 <= k || count1 <= k {
				ans++
			}
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	s := strings.Replace(flds[0], "\"", "", -1)
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("n = \"%s\", k = %d\n", s, k)

	timeStart := time.Now()

	result := countKConstraintSubstrings(s, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

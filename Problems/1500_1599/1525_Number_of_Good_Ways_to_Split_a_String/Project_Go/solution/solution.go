package solution

import (
	"fmt"
	"strings"
	"time"
)

func numSplits(s string) int {
	// 0ms
	var l [26]int
	var r [26]int
	d_l, d_r, res := 0, 0, 0
	for _, ch := range s {
		r[ch-'a']++
		if r[ch-'a'] == 1 {
			d_r++
		}
	}
	for _, ch := range s {
		l[ch-'a']++
		if l[ch-'a'] == 1 {
			d_l++
		}
		r[ch-'a']--
		if r[ch-'a'] == 0 {
			d_r--
		}
		if d_l == d_r {
			res++
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := numSplits(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

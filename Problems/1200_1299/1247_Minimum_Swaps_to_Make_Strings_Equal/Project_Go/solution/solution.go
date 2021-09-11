package solution

import (
	"fmt"
	"strings"
	"time"
)

func minimumSwap(s1 string, s2 string) int {
	// 0ms
	len1, len2 := len(s1), len(s2)
	if len1 != len2 {
		return -1
	}
	x, y, ans := 0, 0, 0
	for i := 0; i < len1; i++ {
		c1, c2 := s1[i], s2[i]
		if c1 != c2 {
			if c1 == 'x' {
				x++
			}
			if c1 == 'y' {
				y++
			}
		}
	}
	ans += x/2 + y/2
	x %= 2
	y %= 2
	if x != y {
		return -1
	}
	return ans + x + y
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	s1, s2 := flds[0], flds[1]
	fmt.Printf("s = \"%s\", s2 = \"%s\"\n", s1, s2)

	timeStart := time.Now()

	result := minimumSwap(s1, s2)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

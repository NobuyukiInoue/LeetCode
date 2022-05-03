package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func digitSum(s string, k int) string {
	// 0ms - 3ms
	for len(s) > k {
		sb := ""
		for i := 0; i < len(s); i += k {
			sm := 0
			for j := i; j < i+k && j < len(s); j++ {
				sm += int(s[j] - '0')
			}
			sb += strconv.Itoa(sm)
		}
		s = sb
	}
	return s
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
	fmt.Printf("s = [%s], k = %d\n", s, k)

	timeStart := time.Now()

	result := digitSum(s, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

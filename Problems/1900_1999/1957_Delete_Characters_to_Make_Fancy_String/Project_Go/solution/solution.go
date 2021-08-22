package solution

import (
	"fmt"
	"strings"
	"time"
)

func makeFancyString(s string) string {
	// 32ms
	ss := []byte(s)
	ans := make([]byte, 0, len(ss))
	cnt := 0
	var lb byte = 0
	for _, b := range ss {
		if b != lb {
			lb = b
			cnt = 1
		} else {
			cnt++
			if cnt > 2 {
				cnt--
				continue
			}
		}
		ans = append(ans, b)
	}
	return string(ans)
}

func makeFancyString2(s string) string {
	// 4572ms
	ans := ""
	cnt := 0
	for i := 0; i < len(s); i++ {
		if i > 0 && s[i-1] == s[i] {
			cnt++
		} else {
			cnt = 1
		}
		if cnt < 3 {
			ans = ans + string(s[i])
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := makeFancyString(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

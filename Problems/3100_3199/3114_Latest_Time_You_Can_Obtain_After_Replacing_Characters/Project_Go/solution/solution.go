package solution

import (
	"fmt"
	"strings"
	"time"
)

func findLatestTime(s string) string {
	// 5ms
	arr_s := []rune(s)
	if arr_s[0] == '?' {
		if arr_s[1] == '?' || arr_s[1] <= '1' {
			arr_s[0] = '1'
		} else {
			arr_s[0] = '0'
		}
	}
	if arr_s[1] == '?' {
		if arr_s[0] == '1' {
			arr_s[1] = '1'
		} else {
			arr_s[1] = '9'
		}
	}
	if arr_s[3] == '?' {
		arr_s[3] = '5'
	}
	if arr_s[4] == '?' {
		arr_s[4] = '9'
	}
	return string(arr_s)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = \"%s\"\n", s)

	timeStart := time.Now()

	result := findLatestTime(s)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

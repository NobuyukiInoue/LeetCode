package solution

import (
	"fmt"
	"strings"
	"time"
)

func getSmallestString(s string) string {
	// 0ms
	arr_s := []byte(s)
	for i := 0; i < len(arr_s)-1; i++ {
		m1, m2 := arr_s[i]%2, arr_s[i+1]%2
		if m1 == m2 && arr_s[i] > arr_s[i+1] {
			arr_s[i], arr_s[i+1] = arr_s[i+1], arr_s[i]
			return string(arr_s)
		}
	}
	return s
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = \"%s\"\n", s)

	timeStart := time.Now()

	result := getSmallestString(s)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

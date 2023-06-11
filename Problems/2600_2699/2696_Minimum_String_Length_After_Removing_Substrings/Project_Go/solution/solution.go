package solution

import (
	"fmt"
	"strings"
	"time"
)

func minLength(s string) int {
	// 0ms - 11ms
	n, st := len(s), make([]byte, 0)
	st = append(st, s[0])
	for i := 1; i < n; i++ {
		if len(st) > 0 && ((s[i] == 'B' && st[len(st)-1] == 'A') || (s[i] == 'D' && st[len(st)-1] == 'C')) {
			st = st[0 : len(st)-1]
		} else {
			st = append(st, s[i])
		}
	}
	return len(st)
}

func minLength2(s string) int {
	// 3ms
	arr_s, i := []rune(s), 0
	for i < len(arr_s)-1 {
		if arr_s[i] == 'A' && arr_s[i+1] == 'B' {
			arr_s = append(arr_s[:i], arr_s[i+2:]...)
			i = myMax(0, i-1)
		} else if arr_s[i] == 'C' && arr_s[i+1] == 'D' {
			arr_s = append(arr_s[:i], arr_s[i+2:]...)
			i = myMax(0, i-1)
		} else {
			i++
		}
	}
	return len(arr_s)
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := minLength(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

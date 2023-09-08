package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func canBeEqual(s1 string, s2 string) bool {
	// 0ms
	if s1 == s2 {
		return true
	}
	arr_s1 := []byte(s1)
	for i := 0; i < 2; i++ {
		if arr_s1[i] == s2[i+2] {
			arr_s1[i], arr_s1[i+2] = arr_s1[i+2], arr_s1[i]
		}
		if string(arr_s1) == s2 {
			return true
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	s1, s2 := flds[0], flds[1]
	fmt.Printf("s1 = \"%s\", s2 = \"%s\"\n", s1, s2)

	timeStart := time.Now()

	result := canBeEqual(s1, s2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

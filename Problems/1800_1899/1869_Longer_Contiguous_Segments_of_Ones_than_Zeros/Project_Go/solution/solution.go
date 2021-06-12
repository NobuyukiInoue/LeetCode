package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func checkZeroOnes(s string) bool {
	// 0ms
	c0, c1, max_c0, max_c1 := 0, 0, 0, 0
	for _, ch := range s {
		if ch == '1' {
			c0 = 0
			c1++
			max_c1 = myMax(max_c1, c1)
		} else {
			c1 = 0
			c0++
			max_c0 = myMax(max_c0, c0)
		}
	}
	return max_c1 > max_c0
}

func myMax(a int, b int) int {
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

	result := checkZeroOnes(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

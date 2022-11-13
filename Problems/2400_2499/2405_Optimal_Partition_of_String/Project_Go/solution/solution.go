package solution

import (
	"fmt"
	"strings"
	"time"
)

func partitionString(s string) int {
	// 16ms - 18ms
	bit, ans := 0, 1
	for _, ch := range s {
		shift := ch - 'a'
		if bit&(1<<shift) != 0 {
			ans++
			bit = 0
		}
		bit |= 1 << shift
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

	result := partitionString(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

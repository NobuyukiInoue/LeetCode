package solution

import (
	"fmt"
	"strings"
	"time"
)

func maximumScore(a int, b int, c int) int {
	// 0ms
	return myMin((a+b+c)/2, a+b+c-myMax3(a, b, c))
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func myMax3(a int, b int, c int) int {
	if a >= b && a >= c {
		return a
	} else if b >= a && b >= c {
		return b
	}
	return c
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	a, b, c := nums[0], nums[1], nums[2]
	fmt.Printf("a = %d, b = %d, c = %d\n", a, b, c)

	timeStart := time.Now()

	result := maximumScore(a, b, c)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

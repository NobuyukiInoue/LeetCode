package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func maximumSwap(num int) int {
	// 0ms
	max := 0
	for p := 1; p <= num; p *= 10 {
		for q := p; q <= num; q *= 10 {
			max = myMax(max, num+num/p%10*(q-p)+num/q%10*(p-q))
		}
	}
	return max
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	num, _ := strconv.Atoi(flds)
	fmt.Printf("num = %d\n", num)

	timeStart := time.Now()

	result := maximumSwap(num)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

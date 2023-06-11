package solution

import (
	"fmt"
	"strings"
	"time"
)

func removeTrailingZeros(num string) string {
	// 4ms - 6ms
	return strings.Trim(num, "0")
}

func removeTrailingZeros2(num string) string {
	// 6ms - 9ms
	var i int
	for i = len(num) - 1; i >= 0 && num[i] == '0'; i-- {
	}
	return num[0 : i+1]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	num := strings.Replace(temp, "]", "", -1)
	fmt.Printf("num = \"%s\"\n", num)

	timeStart := time.Now()

	result := removeTrailingZeros(num)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

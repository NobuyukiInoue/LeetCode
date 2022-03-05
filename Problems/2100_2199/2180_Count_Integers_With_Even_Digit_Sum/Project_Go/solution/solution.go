package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func countEven(num int) int {
	// 0ms
	k, total := num, 0
	num -= num % 10
	for num > 0 {
		total += num % 10
		num /= 10
	}
	if total%2 == 0 {
		return k / 2
	}
	return (k+1)/2 - 1
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	num, _ := strconv.Atoi(flds)
	fmt.Printf("num = %d\n", num)

	timeStart := time.Now()

	result := countEven(num)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

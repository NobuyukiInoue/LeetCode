package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func numberOfSteps(num int) int {
	// 0ms
	count := 0
	for num > 0 {
		if num%2 == 0 {
			num /= 2
		} else {
			num--
		}
		count++
	}
	return count
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)

	num, _ := strconv.Atoi(fld)

	fmt.Printf("num = %d\n", num)
	timeStart := time.Now()

	result := numberOfSteps(num)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

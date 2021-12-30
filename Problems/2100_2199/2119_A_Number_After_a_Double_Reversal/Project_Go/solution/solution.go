package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isSameAfterReversals(num int) bool {
	// 0ms
	return num == 0 || num%10 != 0
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	num, _ := strconv.Atoi(flds)
	fmt.Printf("num = %d\n", num)

	timeStart := time.Now()

	result := isSameAfterReversals(num)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strings"
	"time"
)

func countOperations(num1 int, num2 int) int {
	// 0ms
	res := 0
	for num1 != 0 && num2 != 0 {
		if num1 >= num2 {
			num1 -= num2
		} else {
			num2 -= num1
		}
		res++
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	num1, num2 := nums[0], nums[1]
	fmt.Printf("num1 = %d, num2 = %d\n", num1, num2)

	timeStart := time.Now()

	result := countOperations(num1, num2)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

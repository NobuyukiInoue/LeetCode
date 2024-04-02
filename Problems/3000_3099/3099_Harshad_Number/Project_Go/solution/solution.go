package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func sumOfTheDigitsOfHarshadNumber(x int) int {
	// 1ms
	smDigits, temp_x := 0, x
	for temp_x > 0 {
		smDigits += temp_x % 10
		temp_x /= 10
	}
	if x%smDigits == 0 {
		return smDigits
	}
	return -1
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	x, _ := strconv.Atoi(flds)
	fmt.Printf("x = %d\n", x)

	timeStart := time.Now()

	result := sumOfTheDigitsOfHarshadNumber(x)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

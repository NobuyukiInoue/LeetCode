package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func maximum69Number(num int) int {
	// 0ms
	r, _ := strconv.Atoi((strings.Replace(strconv.Itoa(num), "6", "9", 1)))
	return r
}

func maximum69Number2(num int) int {
	// 0ms
	max := num
	nums := fmt.Sprintf("%d", num)
	for i := range nums {
		if string(nums[i]) == "9" {
			continue
		}

		x, _ := strconv.Atoi(nums[:i] + "9" + nums[i+1:])
		if x > max {
			max = x
		}
	}

	return max
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

	result := maximum69Number(num)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

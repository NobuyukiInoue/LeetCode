package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func canAliceWin(nums []int) bool {
	// 3ms - 5ms
	s_digits, d_digits := 0, 0
	for _, num := range nums {
		if num < 10 {
			s_digits += num
		} else if num < 100 {
			d_digits += num
		}
	}
	if s_digits == d_digits {
		return false
	} else {
		return true
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := canAliceWin(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func hasTrailingZeros(nums []int) bool {
	// 2ms
	cnt := 0
	for _, num := range nums {
		if num%2 == 0 {
			cnt++
			if cnt == 2 {
				return true
			}
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := hasTrailingZeros(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func check(nums []int) bool {
	// 0ms
	k, n := 0, len(nums)
	for i := 0; i < n; i++ {
		if nums[i] > nums[(i+1)%n] {
			k++
		}
		if k > 1 {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := check(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strings"
	"time"
)

func minimumRightShifts(nums []int) int {
	// 0ms - 3ms
	n, ind, pos := len(nums), 0, 0
	for i := 1; i < n; i++ {
		if nums[i-1] > nums[i] {
			ind = i
			pos++
		}
	}
	if pos > 1 {
		return -1
	}
	if ind == 0 {
		return 0
	}
	if nums[n-1] > nums[0] {
		return -1
	}
	return n - ind
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := minimumRightShifts(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

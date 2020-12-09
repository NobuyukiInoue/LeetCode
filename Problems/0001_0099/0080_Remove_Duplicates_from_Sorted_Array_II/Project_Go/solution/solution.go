package solution

import (
	"fmt"
	"strings"
	"time"
)

func removeDuplicates(nums []int) int {
	// 4ms
	numsLen := len(nums)
	if numsLen < 3 {
		return numsLen
	}
	j := 0
	for i := 0; i < numsLen-2; i++ {
		if nums[i] != nums[i+2] {
			nums[j] = nums[i]
			j++
		}
	}
	nums[j] = nums[numsLen-2]
	j++
	nums[j] = nums[numsLen-1]
	j++

	return j
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := removeDuplicates(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

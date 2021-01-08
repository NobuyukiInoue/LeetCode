package solution

import (
	"fmt"
	"strings"
	"time"
)

func singleNonDuplicate(nums []int) int {
	// 4ms
	i := 0
	for i < len(nums)-1 {
		if nums[i] != nums[i+1] {
			return nums[i]
		}
		i += 2
	}
	return nums[i]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums   = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := singleNonDuplicate(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

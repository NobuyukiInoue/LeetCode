package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func maximumGap(nums []int) int {
	// 4ms
	sort.Sort(sort.IntSlice(nums))
	max := 0
	for i := 0; i < len(nums)-1; i++ {
		temp := nums[i+1] - nums[i]
		if temp > max {
			max = temp
		}
	}

	return max
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

	result := maximumGap(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

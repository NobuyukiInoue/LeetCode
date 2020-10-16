package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func specialArray(nums []int) int {
	// 0ms
	sort.Sort(sort.IntSlice(nums))
	for i := 0; i < len(nums); i++ {
		n := len(nums) - i
		cond1 := n <= nums[i]
		cond2 := (i-1 < 0) || (n > nums[i-1])
		if cond1 && cond2 {
			return n
		}
	}
	return -1
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

	result := specialArray(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

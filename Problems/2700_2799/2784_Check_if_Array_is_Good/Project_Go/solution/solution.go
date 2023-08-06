package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func isGood(nums []int) bool {
	// 3ms - 4ms
	if len(nums) < 2 {
		return false
	}
	sort.Sort(sort.IntSlice(nums))
	var i int
	prev := nums[0]
	for i = 1; i < len(nums)-1; i++ {
		if nums[i] != prev+1 {
			return false
		}
		prev = nums[i]
	}
	if nums[i] == len(nums)-1 && nums[i-1] == nums[i] {
		return true
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := isGood(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

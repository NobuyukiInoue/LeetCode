package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func triangleType(nums []int) string {
	// 0ms
	sort.Sort(sort.IntSlice(nums))
	if nums[0]+nums[1] <= nums[2] {
		return "none"
	} else if nums[0] == nums[1] && nums[1] == nums[2] {
		return "equilateral"
	} else if nums[0] == nums[1] || nums[1] == nums[2] {
		return "isosceles"
	} else {
		return "scalene"
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := triangleType(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

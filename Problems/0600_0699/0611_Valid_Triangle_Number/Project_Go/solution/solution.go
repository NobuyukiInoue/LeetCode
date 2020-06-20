package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func triangleNumber(nums []int) int {
	// 4ms
	sort.Sort(sort.IntSlice(nums))
	count, nums_length := 0, len(nums)
	for i := nums_length - 1; i >= 2; i-- {
		l, r := 0, i-1
		for l < r {
			if nums[l]+nums[r] > nums[i] {
				count += r - l
				r--
			} else {
				l++
			}
		}
	}

	return count
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

	result := triangleNumber(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

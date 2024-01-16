package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func missingInteger(nums []int) int {
	// 0ms
	n, total := len(nums), nums[0]
	for i := 1; i < n; i++ {
		if nums[i-1]+1 == nums[i] {
			total += nums[i]
		} else {
			break
		}
	}
	sort.Sort(sort.IntSlice(nums))
	for _, num := range nums {
		if num == total {
			total++
		}
	}
	return total
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := missingInteger(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

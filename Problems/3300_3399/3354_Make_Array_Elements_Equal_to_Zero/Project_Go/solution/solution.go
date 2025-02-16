package solution

import (
	"fmt"
	"strings"
	"time"
)

func countValidSelections(nums []int) int {
	// 0ms
	left, right, index := 0, 0, 0
	for i := 0; i < len(nums); i++ {
		left += nums[i]
		if nums[i] == 0 {
			index = i
			break
		}
	}
	for i := index; i < len(nums); i++ {
		right += nums[i]
	}
	count := 0
	for i := index; i < len(nums); i++ {
		left += nums[i]
		right -= nums[i]
		if nums[i] != 0 {
			continue
		}
		if left == right {
			count += 2
		} else if left-1 == right || left+1 == right {
			count++
		}
	}
	return count
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := countValidSelections(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

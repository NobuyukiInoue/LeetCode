package solution

import (
	"fmt"
	"strings"
	"time"
)

func semiOrderedPermutation(nums []int) int {
	// 3ms - 5ms
	pos1, pos2, n := 0, 0, len(nums)
	for i := 0; i < n; i++ {
		if nums[i] == 1 {
			pos1 = i
		} else if nums[i] == n {
			pos2 = i
		}
	}
	if pos1 > pos2 {
		return pos1 + n - 1 - pos2 - 1
	}
	return pos1 + n - 1 - pos2
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := semiOrderedPermutation(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

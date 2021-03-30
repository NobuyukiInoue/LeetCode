package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func longestConsecutive(nums []int) int {
	// 4ms
	sort.Sort(sort.IntSlice(nums))
	if len(nums) == 1 {
		return 1
	}
	current, maxIndex := 1, 0
	for i := 0; i < len(nums) - 1; i++ {
		if nums[i + 1]  == nums[i] + 1 {
			current++
		} else if nums[i + 1] == nums[i] {
			
		} else {
			current = 1
		}
		maxIndex = myMax(current, maxIndex)
	}
	return maxIndex
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := longestConsecutive(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

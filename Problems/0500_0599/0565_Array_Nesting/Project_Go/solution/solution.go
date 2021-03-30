package solution

import (
	"fmt"
	"strings"
	"time"
)

func arrayNesting(nums []int) int {
	// 12ms
	res := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != -1 {
			j, count := i, 0
			for nums[j] != -1 {
				count++
				nums[j], j = -1, nums[j]
			}
			res = myMax(res, count)
		}
	}
	return res
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

	result := arrayNesting(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

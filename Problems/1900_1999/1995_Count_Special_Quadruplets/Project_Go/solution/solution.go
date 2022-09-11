package solution

import (
	"fmt"
	"strings"
	"time"
)

func countQuadruplets(nums []int) int {
	// 3ms - 14ms
	res, len := 0, len(nums)
	count := make(map[int]int)
	count[nums[len-1]-nums[len-2]] = 1
	for b := len - 3; b >= 1; b-- {
		for a := b - 1; a >= 0; a-- {
			res += count[nums[a]+nums[b]]
		}
		for x := len - 1; x > b; x-- {
			count[nums[x]-nums[b]] = count[nums[x]-nums[b]] + 1
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := countQuadruplets(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

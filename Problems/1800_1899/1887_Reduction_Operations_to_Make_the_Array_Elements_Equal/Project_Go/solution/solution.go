package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func reductionOperations(nums []int) int {
	// 182ms - 203ms
	sort.Ints(nums)
	res, cnt := 0, 0
	for i := 1; i < len(nums); i++ {
		if nums[i] > nums[i-1] {
			cnt++
		}
		res += cnt
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := reductionOperations(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

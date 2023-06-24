package solution

import (
	"fmt"
	"math"
	"sort"
	"strings"
	"time"
)

func findNonMinOrMax(nums []int) int {
	// 67ms - 86ms
	if len(nums) < 3 {
		return -1
	}
	mi, ma := math.MaxInt64, -1
	for _, num := range nums {
		mi = myMin(mi, num)
		ma = myMax(ma, num)
	}
	for _, num := range nums {
		if num != mi && num != ma {
			return num
		}
	}
	return -1
}

func myMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func findNonMinOrMax2(nums []int) int {
	// 94ms - 107ms
	if len(nums) < 3 {
		return -1
	}
	sort.Sort(sort.IntSlice(nums))
	return nums[1]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := findNonMinOrMax(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

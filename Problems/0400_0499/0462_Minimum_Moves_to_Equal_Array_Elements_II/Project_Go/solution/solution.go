package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func minMoves2(nums []int) int {
	// 4ms - 23ms
	sort.Sort(sort.IntSlice(nums))
	mid := nums[len(nums)/2]
	ans := 0
	for _, num := range nums {
		ans += myAbs(num - mid)
	}
	return ans
}

func myAbs(num int) int {
	if num >= 0 {
		return num
	}
	return -num
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := minMoves2(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

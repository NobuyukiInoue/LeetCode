package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func targetIndices(nums []int, target int) []int {
	// 0ms
	sort.Sort(sort.IntSlice(nums))
	var ans []int
	for i, num := range nums {
		if num == target {
			ans = append(ans, i)
		}
	}
	return ans
}

func targetIndices2(nums []int, target int) []int {
	// 4ms
	sort.Ints(nums)
	var ans []int
	for i, num := range nums {
		if num == target {
			ans = append(ans, i)
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	nums := StringToIntArray(flds[0])
	target, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = %s, target = %d\n", IntArrayToString(nums), target)

	timeStart := time.Now()

	result := targetIndices(nums, target)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

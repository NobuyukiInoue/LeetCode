package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func countPairs(nums []int, target int) int {
	// 0ms
	sort.Sort(sort.IntSlice(nums))
	n, ans := len(nums), 0
	for i := 0; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			if nums[i]+nums[j] >= target {
				break
			}
			ans++
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	target, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = [%s], target = %d\n", IntArrayToString(nums), target)

	timeStart := time.Now()

	result := countPairs(nums, target)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

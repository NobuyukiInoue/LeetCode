package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func minimumDifference(nums []int, k int) int {
	// 16ms
	sort.Ints(sort.IntSlice(nums))
	ans := nums[k-1] - nums[0]
	for i := k; i < len(nums); i++ {
		ans = myMin(ans, nums[i]-nums[i-k+1])
	}
	return ans
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = %s, k = %d\n", IntArrayToString(nums), k)

	timeStart := time.Now()

	result := minimumDifference(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func smallestRangeII(nums []int, k int) int {
	// 17ms
	n := len(nums)
	sort.Sort(sort.IntSlice(nums))
	score := nums[n-1] - nums[0]
	res := score
	for i := 0; i < n-1; i++ {
		v_max := myMax(nums[i]+k, nums[n-1]-k)
		v_min := myMin(nums[i+1]-k, nums[0]+k)
		score = v_max - v_min
		res = myMin(res, score)
	}
	return res
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func myMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = [%s], k = %d\n", IntArrayToString(nums), k)

	timeStart := time.Now()

	result := smallestRangeII(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func countKDifference(nums []int, k int) int {
	// 4ms
	pairs, n := 0, len(nums)
	dic := make(map[int]int, 0)
	for i := 0; i < n; i++ {
		pairs += dic[nums[i]+k]
		pairs += dic[nums[i]-k]
		dic[nums[i]] = dic[nums[i]] + 1
	}
	return pairs
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

	result := countKDifference(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

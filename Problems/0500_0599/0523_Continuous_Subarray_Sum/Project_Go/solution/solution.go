package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func checkSubarraySum(nums []int, k int) bool {
	// 144ms
	tmp := make(map[int]int)
	tmp[0] = -1
	sum := 0
	for i := 0; i < len(nums); i++ {
		sum += nums[i]
		if k != 0 {
			sum %= k
		}
		if prevIndex, ok := tmp[sum]; ok {
			if i-prevIndex > 1 {
				return true
			}
		} else {
			tmp[sum] = i
		}
	}
	return false
}

/*
func checkSubarraySum2(nums []int, k int) bool {
	// 1776ms
	dp := make([]int, 0)
	step, accum := 0, 0
	for _, num := range nums {
		accum = (accum + num) % k
		if contains(dp, accum) {
			return true
		}
		dp = append(dp, step)
		step = accum
	}
	return false
}

func contains(nums []int, target int) bool {
	for _, v := range nums {
		if target == v {
			return true
		}
	}
	return false
}
*/

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = [%s], k = %d\n", IntArrayToString(nums), k)

	timeStart := time.Now()

	result := checkSubarraySum(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

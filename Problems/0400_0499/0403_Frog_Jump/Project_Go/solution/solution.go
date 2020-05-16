package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func canCross(stones []int) bool {
	// 4ms
	step := 1
	for i := 0; i < len(stones)-1; i++ {
		if stones[i+1]-stones[i] > step {
			return false
		}
		step++
	}

	return helper(stones, 1, stones[len(stones)-1], 1)
}

func helper(stones []int, start int, end int, step int) bool {
	if start == end {
		return true
	}
	if !contains(stones, start) {
		return false
	}
	if helper(stones, start+step+1, end, step+1) {
		return true
	}
	if helper(stones, start+step, end, step) {
		return true
	}
	if step > 1 && helper(stones, start+step-1, end, step-1) {
		return true
	}
	return false
}

func contains(nums []int, target int) bool {
	for _, n := range nums {
		if n == target {
			return true
		}
	}
	return false
}

func strToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intArrayToString(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	stones := strToIntArray(flds)
	fmt.Printf("stones = [%s]\n", intArrayToString(stones))

	timeStart := time.Now()

	result := canCross(stones)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

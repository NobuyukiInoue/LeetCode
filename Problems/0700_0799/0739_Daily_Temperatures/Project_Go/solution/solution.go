package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func dailyTemperatures(T []int) []int {
	// 48ms
	stack := make([]int, len(T))
	top := -1
	ret := make([]int, len(T))
	for i := 0; i < len(T); i++ {
		for top > -1 && T[i] > T[stack[top]] {
			idx := stack[top]
			top--
			ret[idx] = i - idx
		}
		top++
		stack[top] = i
	}
	return ret
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
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	T := strToIntArray(flds)
	fmt.Printf("T = [%s]\n", intArrayToString(T))

	timeStart := time.Now()

	result := dailyTemperatures(T)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", intArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

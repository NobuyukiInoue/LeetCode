package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func shipWithinDays(weights []int, D int) int {
	// 32ms
	left, right := 0, 0
	for _, w := range weights {
		left = myMax(left, w)
		right += w
	}
	for left < right {
		mid := (left + right) / 2
		need := 1
		cur := 0
		for _, w := range weights {
			if cur+w > mid {
				need += 1
				cur = 0
			}
			cur += w
		}
		if need > D {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
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
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	weights := strToIntArray(flds[0])
	D, _ := strconv.Atoi(flds[1])

	fmt.Printf("weights = [%s], D = %d\n", intArrayToString(weights), D)

	timeStart := time.Now()

	result := shipWithinDays(weights, D)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

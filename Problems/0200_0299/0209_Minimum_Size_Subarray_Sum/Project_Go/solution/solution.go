package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func minSubArrayLen(s int, nums []int) int {
	// 4ms
	i, n := 0, len(nums)
	res := n + 1
	for j := 0; j < n; j++ {
		s -= nums[j]
		for s <= 0 {
			res = myMin(res, j-i+1)
			s += nums[i]
			i++
		}
	}
	return res % (n + 1)
}

func myMin(a int, b int) int {
	if a <= b {
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

func intArrayToString(arr []int) string {
	if len(arr) <= 0 {
		return ""
	}

	resultStr := "["
	for i := 0; i < len(arr); i++ {
		if i > 0 {
			resultStr += ","
		}
		resultStr += strconv.Itoa(arr[i])
	}

	return resultStr + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	s, _ := strconv.Atoi(flds[0])
	nums := strToIntArray(flds[1])

	fmt.Printf("s = %d, nums = %s\n", s, intArrayToString(nums))

	timeStart := time.Now()

	result := minSubArrayLen(s, nums)
	fmt.Printf("result = %d\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

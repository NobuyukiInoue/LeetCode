package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func maximum69Number(num int) int {
	// 0ms
	r, _ := strconv.Atoi((strings.Replace(strconv.Itoa(num), "6", "9", 1)))
	return r
}

func maximum69Number2(num int) int {
	// 0ms
	max := num
	nums := fmt.Sprintf("%d", num)
	for i := range nums {
		if string(nums[i]) == "9" {
			continue
		}

		x, _ := strconv.Atoi(nums[:i] + "9" + nums[i+1:])
		if x > max {
			max = x
		}
	}

	return max
}

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intintArrayToString(nums [][]int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := "[" + intArrayToString(nums[0]) + "]"
	for i := 1; i < len(nums); i++ {
		resultStr += ", [" + intArrayToString(nums[i]) + "]"
	}

	return resultStr
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
	fld := strings.Replace(temp, "]", "", -1)

	num, _ := strconv.Atoi(fld)
	fmt.Printf("num = %d\n", num)

	timeStart := time.Now()

	result := maximum69Number(num)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

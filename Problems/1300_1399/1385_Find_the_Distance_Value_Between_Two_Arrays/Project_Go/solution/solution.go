package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findTheDistanceValue(arr1 []int, arr2 []int, d int) int {
	// 4ms
	res := 0
	for i := 0; i < len(arr1); i++ {
		for j := 0; j < len(arr2); j++ {
			if myAbs(arr1[i]-arr2[j]) <= d {
				break
			}

			if j == len(arr2)-1 {
				res++
			}
		}
	}
	return res
}

func myAbs(val int) int {
	if val >= 0 {
		return val
	}

	return -val
}

func myMin(a int, b int) int {
	if a < b {
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
		return "[]"
	}

	resultStr := "[" + strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
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

	arr1 := strToIntArray(flds[0])
	arr2 := strToIntArray(flds[1])
	d, _ := strconv.Atoi(flds[2])
	fmt.Printf("arr1 = %s, arr2 = %s, d = %d\n", intArrayToString(arr1), intArrayToString(arr2), d)

	timeStart := time.Now()

	result := findTheDistanceValue(arr1, arr2, d)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

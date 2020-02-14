package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func getNoZeroIntegers(n int) []int {
	// 4ms
	for a := 1; a < n; a++ {
		b := n - a
		if strings.Index(strconv.Itoa(a), "0") < 0 && strings.Index(strconv.Itoa(b), "0") < 0 {
			return []int{a, b}
		}
	}
	return []int{}
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

	n, _ := strconv.Atoi(fld)

	fmt.Printf("n = %d\n", n)
	timeStart := time.Now()

	result := getNoZeroIntegers(n)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", intArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

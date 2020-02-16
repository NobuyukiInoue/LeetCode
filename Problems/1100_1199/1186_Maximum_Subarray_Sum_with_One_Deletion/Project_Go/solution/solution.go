package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func maximumSum(arr []int) int {
	// 24ms
	arrLength := len(arr)
	withDelete := make([]int, arrLength)
	withOutDelete := make([]int, arrLength)
	start, result := 0, math.MinInt64
	for start < arrLength && arr[start] < 0 {
		result = myMax(result, arr[start])
		start++
	}

	for i := start; i < arrLength; i++ {
		if arr[i] >= 0 {
			if i == 0 {
				withOutDelete[i] = arr[i]
				withDelete[i] = arr[i]
			} else {
				withOutDelete[i] = myMax(withOutDelete[i-1]+arr[i], arr[i])
				withDelete[i] = myMax(withDelete[i-1]+arr[i], arr[i])
			}
		} else { //negative number:
			if i > 0 {
				withOutDelete[i] = myMax(withOutDelete[i-1]+arr[i], arr[i])
				withDelete[i] = myMax(withOutDelete[i-1], withDelete[i-1]+arr[i])
			}
		}
		result = myMax(result, withOutDelete[i])
		result = myMax(result, withDelete[i])
	}

	return result
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
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	arr := strToIntArray(flds)
	fmt.Printf("arr = %s\n", intArrayToString(arr))

	timeStart := time.Now()

	result := maximumSum(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func duplicateZeros(arr []int) {
	// 32ms
	helper(arr, 0)
}

func helper(arr []int, cnt int) {
	if len(arr) <= cnt {
		return
	}
	i := 0
	for i = 0; i < len(arr); i++ {
		if arr[i] == 0 {
			break
		}
	}
	if i != len(arr) {
		helper(arr[i+1:], cnt+1)
	}
	if i+cnt+1 < len(arr) {
		arr[i+cnt+1] = 0
	}
	for j := min(i, len(arr)-cnt-1); j >= 0; j-- {
		arr[j+cnt] = arr[j]
	}
}

func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func duplicateZeros2(arr []int) {
	// 44ms
	countZero := 0
	for i := 0; i < len(arr); i++ {
		if arr[i] == 0 {
			countZero++
		}
	}
	arrLen := len(arr) + countZero
	for i, j := len(arr)-1, arrLen-1; i < j; i-- {
		if arr[i] != 0 {
			if j < len(arr) {
				arr[j] = arr[i]
			}
		} else {
			if j < len(arr) {
				arr[j] = arr[i]
			}
			j--
			if j < len(arr) {
				arr[j] = arr[i]
			}
		}
		j--
	}
}

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func printIntArray(nums []int) string {
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
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	arr := make([]int, len(flds))
	for i := 0; i < len(flds); i++ {
		arr[i], _ = strconv.Atoi(flds[i])
	}

	fmt.Printf("arr = %s\n", printIntArray(arr))
	timeStart := time.Now()

	duplicateZeros(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", printIntArray(arr))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

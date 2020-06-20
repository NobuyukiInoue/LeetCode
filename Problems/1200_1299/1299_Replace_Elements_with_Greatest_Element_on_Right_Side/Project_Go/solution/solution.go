package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func replaceElements(arr []int) []int {
	// 788ms
	mx := -1
	for i := len(arr) - 1; i >= 0; i-- {
		arr[i], mx = mx, Max(arr[i], mx)
	}
	return arr
}

func Max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func StringToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func IntArrayToString(nums []int) string {
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

	arr := StringToIntArray(flds)
	fmt.Printf("arr = %s\n", IntArrayToString(arr))

	timeStart := time.Now()

	result := replaceElements(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

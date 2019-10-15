package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func checkPossibility(nums []int) bool {
	count_dec := 0
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] > nums[i+1] {
			count_dec++
			if i == 0 {
				nums[i] = nums[i+1]
			} else if nums[i-1] <= nums[i+1] {
				nums[i] = nums[i-1]
			} else {
				nums[i+1] = nums[i]
			}
		}
		if count_dec > 1 {
			return false
		}
	}

	return true
}

func IntArray2string(arr []int) string {
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
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	nums := make([]int, len(flds))
	for i, _ := range flds {
		nums[i], _ = strconv.Atoi(flds[i])
	}

	fmt.Printf("nums = %s\n", IntArray2string(nums))

	timeStart := time.Now()

	result := checkPossibility(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

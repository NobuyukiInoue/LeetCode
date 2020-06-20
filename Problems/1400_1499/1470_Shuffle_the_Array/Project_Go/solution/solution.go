package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func shuffle(nums []int, n int) []int {
	// 4ms
	res := make([]int, len(nums))
	mid := len(nums) / 2
	for i := 0; i < mid; i++ {
		res[2*i] = nums[i]
		res[2*i+1] = nums[mid+i]
	}
	return res
}

func boolArrayToString(data []bool) string {
	if len(data) <= 0 {
		return ""
	}

	resultStr := strconv.FormatBool(data[0])
	for i := 1; i < len(data); i++ {
		resultStr += ", " + strconv.FormatBool(data[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	nums := StringToIntArray(flds[0])
	n, _ := strconv.Atoi(flds[1])

	fmt.Printf("nums = [%s], n = %d\n", IntArrayToString(nums), n)

	timeStart := time.Now()

	result := shuffle(nums, n)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

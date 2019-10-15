package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func majorityElement(nums []int) int {
	// 16ms
	var count, value int

	for i := range nums {
		if count == 0 {
			value = nums[i]
		}
		if value == nums[i] {
			count++
		} else {
			count--
		}
	}

	return value
}

func majorityElement2(nums []int) int {
	// 20ms
	sort.Sort(sort.IntSlice(nums))
	return nums[len(nums)/2]
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
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	nums := str2IntArray(flds)

	fmt.Printf("nums[] = %s\n", printIntArray(nums))

	timeStart := time.Now()

	result := majorityElement(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

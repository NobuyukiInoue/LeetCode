package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func minOperations(nums []int, k int) int {
	// 3ms - 4ms
	min, elems := nums[0], map[int]bool{}
	for _, num := range nums {
		if num > k {
			elems[num] = true
			min = myMin(min, num)
		} else if num < k {
			return -1
		}
	}
	if min < k {
		return -1
	}
	return len(elems)
}

func myMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = [%s], k = %d\n", IntArrayToString(nums), k)

	timeStart := time.Now()

	result := minOperations(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

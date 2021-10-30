package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func splitArray(nums []int, m int) int {
	// 0ms
	start, end := 0, 0
	for _, num := range nums {
		start = myMax(start, num)
		end += num
	}
	for start < end {
		mid := start + (end-start)/2
		total, pieces := 0, 1
		for _, num := range nums {
			if total+num > mid {
				total = num
				pieces++
			} else {
				total += num
			}
		}
		if pieces > m {
			start = mid + 1
		} else {
			end = mid
		}
	}
	return end
}

func myMax(a int, b int) int {
	if a > b {
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
	m, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = %s, k = %d\n", IntArrayToString(nums), m)

	timeStart := time.Now()

	result := splitArray(nums, m)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

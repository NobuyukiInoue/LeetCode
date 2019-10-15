package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func searchRange(nums []int, target int) []int {
	low, high := math.MaxInt32, 0
	hit := false
	for _, cur := range nums {
		if cur == target {
			hit = true
		}
	}
	if !hit {
		return []int{-1, -1}
	}

	for i := 0; i < len(nums); i++ {
		if nums[i] == target {
			if i > high {
				high = i
			}
			if i < low {
				low = i
			}
		}
	}
	return []int{low, high}
}

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intArray2string(arr []int) string {
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
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := str2IntArray(flds[0])
	target, _ := strconv.Atoi(flds[1])

	fmt.Printf("nums = %s\n", intArray2string(nums))
	fmt.Printf("target = %d\n", target)

	timeStart := time.Now()

	result := searchRange(nums, target)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

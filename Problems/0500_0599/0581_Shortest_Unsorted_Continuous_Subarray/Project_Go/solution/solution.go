package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findUnsortedSubarray(nums []int) int {
	maxLoc := 0
	start, end := 0, 0
	counter := 1
	for counter < len(nums) {
		curr := nums[counter]
		if curr >= nums[maxLoc] {
			if start == end {
				start = counter
				end = counter
			}
			maxLoc = counter
		} else if curr < nums[maxLoc] && curr > nums[start] {
			end = counter
		} else {
			for start > 0 && nums[start-1] > curr {
				start--
			}
			end = counter
		}
		counter++
	}
	if end == start {
		return 0
	}
	return end - start + 1
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

	fmt.Printf("candies = %s\n", IntArray2string(nums))

	timeStart := time.Now()

	result := findUnsortedSubarray(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func insert(intervals [][]int, newInterval []int) [][]int {
	// 8ms
	ret := make([][]int, 0)
	for i, v := range intervals {
		if v[1] < newInterval[0] {
			ret = append(ret, v)
			continue
		}

		if v[0] > newInterval[1] {
			ret = append(ret, newInterval)
			ret = append(ret, intervals[i:]...)
			return ret
		}

		newInterval[0] = min(newInterval[0], v[0])
		newInterval[1] = max(newInterval[1], v[1])
	}
	return append(ret, newInterval)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func stringToIntArray(data string) []int {
	flds := strings.Split(data, ",")
	nums := make([]int, len(flds))
	for i, _ := range flds {
		nums[i], _ = strconv.Atoi(flds[i])
	}
	return nums
}

func intArrayToString(arr []int) string {
	if len(arr) <= 0 {
		return ""
	}

	resultStr := ""
	for i := 0; i < len(arr); i++ {
		if i > 0 {
			resultStr += ","
		}
		resultStr += strconv.Itoa(arr[i])
	}

	return resultStr
}

func intintArrayToString(nums [][]int) string {
	resultStr := ""
	for i := 0; i < len(nums); i++ {
		if i == 0 {
			resultStr += "[" + intArrayToString(nums[i]) + "]"
		} else {
			resultStr += ",[" + intArrayToString(nums[i]) + "]"
		}
	}
	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	flds := strings.Split(temp, "]],[")

	data0 := strings.Split(flds[0], "],[")
	intervals := make([][]int, len(data0))
	for i, _ := range data0 {
		intervals[i] = stringToIntArray(data0[i])
	}
	data1 := strings.Replace(flds[1], "]]", "", -1)
	newInterval := stringToIntArray(data1)

	fmt.Printf("intervals = [" + intintArrayToString(intervals) + "]\n")
	fmt.Printf("newInterval = [" + intArrayToString(newInterval) + "]\n")

	timeStart := time.Now()

	result := insert(intervals, newInterval)

	timeEnd := time.Now()

	fmt.Printf("result = [" + intintArrayToString(result) + "]\n")
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

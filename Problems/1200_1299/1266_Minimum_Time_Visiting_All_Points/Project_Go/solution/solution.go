package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func minTimeToVisitAllPoints(points [][]int) int {
	// 4ms
	total := 0
	for i := 1; i < len(points); i++ {
		total += max(abs(points[i][0]-points[i-1][0]), abs(points[i][1]-points[i-1][1]))
	}
	return total
}

func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func abs(a int) int {
	if a >= 0 {
		return a
	} else {
		return -a
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
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	points := make([][]int, len(flds))
	for i := 0; i < len(flds); i++ {
		points[i] = str2IntArray(flds[i])
	}

	fmt.Printf("points = [")
	for i, _ := range points {
		if i == 0 {
			fmt.Printf("[%s]", printIntArray(points[i]))
		} else {
			fmt.Printf(",[%s]", printIntArray(points[i]))
		}
	}
	fmt.Printf("]\n")

	timeStart := time.Now()

	result := minTimeToVisitAllPoints(points)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.Itoa(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

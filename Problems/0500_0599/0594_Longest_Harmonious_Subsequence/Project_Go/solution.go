package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func findLHS(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	sort.Sort(sort.IntSlice(nums))
	start := 0
	nextstart := 0
	res := 0
	for i := 1; i < len(nums); i++ {
		if nums[i]-nums[start] == 1 {
			if nums[nextstart] < nums[i] {
				nextstart = i
			}
			res = IntMax(res, i-start+1)
		} else if nums[i]-nums[start] > 1 {
			if start == nextstart {
				start = i
			} else {
				start = nextstart
			}
			i--
		}
	}
	return res
}

func IntMax(a int, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
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

	result := findLHS(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

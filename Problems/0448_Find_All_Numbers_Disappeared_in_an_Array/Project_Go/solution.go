package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findDisappearedNumbers(nums []int) []int {
	for i := range nums {
		for nums[nums[i]-1] != nums[i] {
			nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
		}
	}

	out := []int{}
	for i, v := range nums {
		if v != i+1 {
			out = append(out, i+1)
		}
	}
	return out
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
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	nums := make([]int, len(flds))
	for i, val := range flds {
		nums[i], _ = strconv.Atoi(val)
	}

	fmt.Printf("nums = %s\n", IntArray2string(nums))

	timeStart := time.Now()

	result := findDisappearedNumbers(nums)
	fmt.Printf("result = %s\n", IntArray2string(result))

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

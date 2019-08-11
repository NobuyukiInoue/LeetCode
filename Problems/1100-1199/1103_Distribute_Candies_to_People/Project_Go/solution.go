package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func distributeCandies(candies int, num_people int) []int {
	res := make([]int, num_people)
	for i := 0; candies > 0; i++ {
		res[i%num_people] += min(candies, i+1)
		candies -= i + 1
	}
	return res
}

func min(a int, b int) int {
	if a < b {
		return a
	} else {
		return b
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
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	candies, _ := strconv.Atoi(flds[0])
	num_people, _ := strconv.Atoi(flds[1])

	fmt.Printf("candies = %d, num_people = %d\n", candies, num_people)
	timeStart := time.Now()

	result := distributeCandies(candies, num_people)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", printIntArray(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

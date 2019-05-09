package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func sumArray(A []int) int {
	sum := 0
	for _, v := range A {
		sum = sum + v
	}
	return sum
}
func fairCandySwap(A []int, B []int) []int {
	sumA := sumArray(A)
	sum := sumA + sumArray(B)
	var mp = make(map[int]int)
	var ans []int
	for k, v := range B {
		mp[v] = k
	}

	for _, v := range A {
		need := sum/2 - (sumA - v)

		if _, ok := mp[need]; ok {
			ans = append(ans, v, need)
			break
		}
	}
	return ans
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

	A := str2IntArray(flds[0])
	B := str2IntArray(flds[1])

	fmt.Printf("A = %s\n", printIntArray(A))
	fmt.Printf("B = %s\n", printIntArray(B))

	timeStart := time.Now()

	result := fairCandySwap(A, B)

	fmt.Printf("result = %s\n", printIntArray(result))

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

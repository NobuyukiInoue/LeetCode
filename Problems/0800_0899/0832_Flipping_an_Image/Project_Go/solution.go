package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func flipAndInvertImage(A [][]int) [][]int {
	n := len(A)
	for _, row := range A {
		for i := 0; i*2 < n; i++ {
			if row[i] == row[n-i-1] {
				row[n-i-1] = row[n-i-1] ^ 1
				row[i] = row[n-i-1]
			}
		}
	}
	return A
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

	fmt.Printf("A = \n")
	A := make([][]int, len(flds))
	for i := 0; i < len(flds); i++ {
		A[i] = str2IntArray(flds[i])
		fmt.Printf("%s\n", printIntArray(A[i]))
	}

	timeStart := time.Now()

	result := flipAndInvertImage(A)

	fmt.Printf("result = \n")
	for i := 0; i < len(result); i++ {
		fmt.Printf("%s\n", printIntArray(result[i]))
	}

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

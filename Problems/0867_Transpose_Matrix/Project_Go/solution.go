package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func transpose(A [][]int) [][]int {
	rowNum := len(A)
	colNum := len(A[0])

	ret := make([][]int, colNum)
	for index := range ret {
		ret[index] = make([]int, rowNum)
	}

	for i := 0; i < colNum; i++ {
		for j := 0; j < rowNum; j++ {
			ret[i][j] = A[j][i]
		}
	}
	return ret
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

	result := transpose(A)

	fmt.Printf("result = \n")
	for i := 0; i < len(result); i++ {
		fmt.Printf("%s\n", printIntArray(result[i]))
	}

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

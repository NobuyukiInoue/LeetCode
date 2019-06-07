package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func largestSumAfterKNegations(A []int, K int) int {
	sort.Sort(sort.IntSlice(A))
	for i, j := 0, 0; i < K; i++ {
		if j+1 < len(A) && A[j+1] < A[j] {
			j++
		}
		A[j] = -A[j]
	}
	sum := 0
	for i := 0; i < len(A); i++ {
		sum += A[i]
	}
	return sum
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

	A := str2IntArray(flds[0])
	K, _ := strconv.Atoi(flds[1])

	fmt.Printf("A = %s\n", intArray2string(A))
	fmt.Printf("K = %d\n", K)

	timeStart := time.Now()

	result := largestSumAfterKNegations(A, K)

	fmt.Printf("result = %d\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

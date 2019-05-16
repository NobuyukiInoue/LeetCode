package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func sortArrayByParityII(A []int) []int {
	// 320ms
	for i, j := 0, 1; i < len(A); i += 2 {
		if A[i]&1 == 0 {
			continue
		}
		for ; A[j]&1 != 0; j += 2 {
		}
		A[i], A[j] = A[j], A[i]
	}
	return A
}

func sortArrayByParityII_2(A []int) []int {
	// 308ms
	even, odd := 0, 1
	for true {
		for even < len(A) && A[even]%2 == 0 {
			even += 2
		}

		for odd < len(A) && A[odd]%2 != 0 {
			odd += 2
		}

		if odd >= len(A) || even >= len(A) {
			return A
		}

		temp := A[even]
		A[even] = A[odd]
		A[odd] = temp
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
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	A := str2IntArray(flds)

	fmt.Printf("A = %s\n", printIntArray(A))

	timeStart := time.Now()

	result := sortArrayByParityII(A)

	fmt.Printf("result = %s\n", printIntArray(result))

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

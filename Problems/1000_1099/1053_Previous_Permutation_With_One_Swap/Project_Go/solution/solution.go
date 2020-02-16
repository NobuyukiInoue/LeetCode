package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func prevPermOpt1(A []int) []int {
	// 32ms
	index, number := -1, 0
	min := math.MaxInt64
	lenA := len(A)

	for i := lenA - 1; i > 0; i-- {
		if A[i] < min {
			min = A[i]
		}
		if min < A[i-1] {
			number = A[i-1]
			index = i
			break
		}
	}

	if index == -1 {
		return A
	}

	maxTemp, indexer := -1, -1
	for i := index; i < lenA; i++ {
		if A[i] > maxTemp && A[i] < number {
			maxTemp = A[i]
			indexer = i
		}
	}

	temper := A[indexer]
	A[indexer] = A[index-1]
	A[index-1] = temper

	return A
}

func strToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intArrayToString(nums []int) string {
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

	A := make([]int, len(flds))
	for i := 0; i < len(flds); i++ {
		A[i], _ = strconv.Atoi(flds[i])
	}

	fmt.Printf("A = %s\n", intArrayToString(A))
	timeStart := time.Now()

	result := prevPermOpt1(A)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", intArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

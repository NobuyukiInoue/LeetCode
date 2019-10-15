package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func smallestRangeI(A []int, K int) int {
	mx, mn := A[0], A[0]
	for _, a := range A {
		mx = max(mx, a)
		mn = min(mn, a)
	}

	return max(0, mx-mn-2*K)
}

func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
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
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	A := str2IntArray(flds[0])
	K, _ := strconv.Atoi(flds[1])

	fmt.Printf("A = %s\n", printIntArray(A))
	fmt.Printf("K = %d\n", K)

	timeStart := time.Now()

	result := smallestRangeI(A, K)

	fmt.Printf("result = %d\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

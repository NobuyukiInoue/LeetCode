package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func bitwiseComplement(N int) int {
	if N == 0 {
		return 1
	}
	temp := 0
	for i := 1; N > temp; i++ {
		temp = pow(2, i)
	}

	if N == temp {
		return N - 1
	} else {
		return temp - 1 - N
	}
}

func pow(x int, y int) int {
	if y == 0 {
		return 1
	}
	result := 1
	for i := 0; i < y; i++ {
		result *= x
	}
	return result
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

	N, _ := strconv.Atoi(flds)
	fmt.Printf("N = %d\n", N)

	timeStart := time.Now()

	result := bitwiseComplement(N)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

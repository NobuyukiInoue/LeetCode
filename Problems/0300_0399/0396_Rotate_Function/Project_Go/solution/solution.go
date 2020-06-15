package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func maxRotateFunction(A []int) int {
	// 8ms
	total := 0
	res := 0
	for i, a := range A {
		total += a
		res += i * a
	}
	temp := res
	for _, a := range A {
		if temp-total+a*len(A) > res {
			res = temp - total + a*len(A)
		}
		temp = temp - total + a*len(A)
	}
	return res
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
	flds := strings.Replace(temp, "]", "", -1)

	A := strToIntArray(flds)
	fmt.Printf("A = [%s]\n", intArrayToString(A))

	timeStart := time.Now()

	result := maxRotateFunction(A)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

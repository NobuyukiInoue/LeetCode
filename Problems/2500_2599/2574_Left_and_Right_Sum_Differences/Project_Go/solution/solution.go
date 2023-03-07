package solution

import (
	"fmt"
	"strings"
	"time"
)

func leftRigthDifference(nums []int) []int {
	// 2ms
	total := 0
	for _, num := range nums {
		total += num
	}
	left, right := 0, total
	ans := make([]int, len(nums))
	for i, num := range nums {
		left += num
		ans[i] = myAbs(left - right)
		right -= num
	}
	return ans
}

func myAbs(n int) int {
	if n > 0 {
		return n
	}
	return -n
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := leftRigthDifference(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

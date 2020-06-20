package solution

import (
	"fmt"
	"strings"
	"time"
)

func pivotIndex(nums []int) int {
	if len(nums) <= 2 {
		return -1
	}

	s, leftSum := 0, 0
	for _, x := range nums {
		s += x
	}

	for i, value := range nums {
		if leftSum*2+value == s {
			return i
		}
		leftSum += value
	}

	return -1
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	nums := StringToIntArray(flds)

	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := pivotIndex(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

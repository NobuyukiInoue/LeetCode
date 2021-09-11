package solution

import (
	"fmt"
	"strings"
	"time"
)

func findGCD(nums []int) int {
	// 4ms
	v_min, v_max := nums[0], nums[0]
	for i := 1; i < len(nums); i++ {
		v_min = myMin(v_min, nums[i])
		v_max = myMax(v_max, nums[i])
	}
	for i := v_min; i > 0; i-- {
		if v_min%i == 0 && v_max%i == 0 {
			return i
		}
	}
	return -1
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := findGCD(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

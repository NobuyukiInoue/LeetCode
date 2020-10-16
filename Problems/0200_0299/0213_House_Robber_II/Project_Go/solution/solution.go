package solution

import (
	"fmt"
	"strings"
	"time"
)

func rob(nums []int) int {
	// 0ms
	if len(nums) <= 0 {
		return 0
	}
	if len(nums) == 1 {
		return nums[0]
	}
	return myMax(rob_sub(nums, 0, len(nums) - 1), rob_sub(nums, 1, len(nums)));
}

func rob_sub(nums []int, start int, end int) int {
	preRob, preNotRob, rob, notRob := 0, 0, 0, 0

	for i := start; i < end; i++ {
		rob = preNotRob + nums[i]
		notRob = myMax(preRob, preNotRob)

		preNotRob = notRob
		preRob = rob
	}
	return myMax(rob, notRob)
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}


func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := rob(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

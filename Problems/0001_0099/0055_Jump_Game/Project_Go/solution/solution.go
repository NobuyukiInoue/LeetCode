package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func canJump(nums []int) bool {
	// 8ms
	if len(nums) < 2 {
		return true
	}

	for curr := len(nums) - 2; curr >= 0; curr-- {
		if nums[curr] == 0 {
			neededJumps := 1
			for neededJumps > nums[curr] {
				neededJumps++
				curr--
				if curr < 0 {
					return false
				}
			}
		}
	}
	return true
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

	result := canJump(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

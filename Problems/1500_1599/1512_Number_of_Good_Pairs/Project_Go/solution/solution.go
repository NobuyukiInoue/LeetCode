package solution

import (
	"fmt"
	"strings"
	"time"
)

func numIdenticalPairs(nums []int) int {
	// 0ms
	count, numsLength := 0, len(nums)
	for i := 0; i < numsLength - 1; i++ {
		for j := i + 1; j < numsLength; j++ {
			if nums[i] == nums[j] {
				count++
			}
		}
	}
	return count;
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

	result := numIdenticalPairs(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

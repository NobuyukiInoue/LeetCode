package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxOperations(nums []int) int {
	// 4ms
	ans, total := 0, nums[0]+nums[1]
	for i := 0; i < len(nums)-1; i += 2 {
		if nums[i]+nums[i+1] != total {
			break
		}
		ans++
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := maxOperations(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

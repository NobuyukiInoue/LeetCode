package solution

import (
	"fmt"
	"strings"
	"time"
)

func countPartitions(nums []int) int {
	// 0ms
	sum_l, sum_r := sum_array(nums), 0
	ans := 0
	for i := 0; i < len(nums)-1; i++ {
		sum_l -= nums[i]
		sum_r += nums[i]
		if (sum_l-sum_r)%2 == 0 {
			ans++
		}
	}
	return ans
}

func sum_array(arr []int) int {
	v_sum := arr[0]
	for i := 1; i < len(arr); i++ {
		v_sum += arr[i]
	}
	return v_sum
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := countPartitions(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

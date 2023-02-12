package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findTheArrayConcVal(nums []int) int64 {
	// 3ms - 6ms
	n, ans := len(nums), int64(0)
	for i := 0; i < n/2; i++ {
		temp, _ := strconv.Atoi(strconv.Itoa(nums[i]) + strconv.Itoa(nums[n-i-1]))
		ans += int64(temp)
	}
	if n%2 == 1 {
		ans += int64(nums[n/2])
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

	result := findTheArrayConcVal(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

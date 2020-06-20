package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findMaxConsecutiveOnes(nums []int) int {
	max, count := 0, 0
	for _, n := range nums {
		if n == 0 {
			count = 0
			continue
		}
		count++
		if count > max {
			max = count
		}
	}
	return max
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	nums := make([]int, len(flds))
	for i, val := range flds {
		nums[i], _ = strconv.Atoi(val)
	}

	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := findMaxConsecutiveOnes(nums)
	fmt.Printf("result = %d\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func searchInsert(nums []int, target int) int {
	// 2ms
	for i, num := range nums {
		if target <= num {
			return i
		}
	}
	return len(nums)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	target, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = [%s], target = %d\n", IntArrayToString(nums), target)

	timeStart := time.Now()

	result := searchInsert(nums, target)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

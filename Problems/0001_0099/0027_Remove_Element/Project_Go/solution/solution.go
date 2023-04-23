package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func removeElement(nums []int, val int) int {
	// 2ms
	j := 0
	for i, _ := range nums {
		if nums[i] != val {
			nums[j] = nums[i]
			j++
		}
	}
	return j
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	val, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = [%s], val = %d\n", IntArrayToString(nums), val)

	timeStart := time.Now()

	result := removeElement(nums, val)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

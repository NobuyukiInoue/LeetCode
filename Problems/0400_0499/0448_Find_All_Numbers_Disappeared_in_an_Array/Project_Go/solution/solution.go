package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findDisappearedNumbers(nums []int) []int {
	for i := range nums {
		for nums[nums[i]-1] != nums[i] {
			nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
		}
	}

	out := []int{}
	for i, v := range nums {
		if v != i+1 {
			out = append(out, i+1)
		}
	}
	return out
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

	result := findDisappearedNumbers(nums)
	fmt.Printf("result = %s\n", IntArrayToString(result))

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

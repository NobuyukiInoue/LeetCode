package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func checkPossibility(nums []int) bool {
	count_dec := 0
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] > nums[i+1] {
			count_dec++
			if i == 0 {
				nums[i] = nums[i+1]
			} else if nums[i-1] <= nums[i+1] {
				nums[i] = nums[i-1]
			} else {
				nums[i+1] = nums[i]
			}
		}
		if count_dec > 1 {
			return false
		}
	}

	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := checkPossibility(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

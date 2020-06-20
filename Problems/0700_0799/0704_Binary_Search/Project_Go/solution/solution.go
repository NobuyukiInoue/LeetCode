package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func search(nums []int, target int) int {
	ans := -1
	lo, hi := 0, len(nums)

	for lo < hi {
		mid := lo + (hi-lo)/2

		if nums[mid] == target {
			ans = mid
			break
		}

		if nums[mid] < target {
			lo = mid + 1
		}

		if nums[mid] > target {
			hi = mid
		}
	}

	return ans
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

	result := search(nums, target)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func search(nums []int, target int) bool {
	// 8ms
	left, right := 0, len(nums) - 1

	for left <=  right {
		mid := (left + right) / 2
		if nums[mid] == target {
			return true
		}
		if nums[left] <= nums[mid] {
			if nums[left] == nums[mid] && mid != left {
				left++
				continue
			}
			if nums[left] <= target && target < nums[mid] {
				right = mid - 1
			} else {
				left = mid + 1
			}
		} else if nums[left] > nums[mid] {
			if nums[mid] < target && target <= nums[right] {
				left = mid + 1
			} else {
				right = mid - 1
			}
		}
	}

	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	target, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = [%s], target = %d\n", IntArrayToString(nums), target)

	timeStart := time.Now()

	result := search(nums, target)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

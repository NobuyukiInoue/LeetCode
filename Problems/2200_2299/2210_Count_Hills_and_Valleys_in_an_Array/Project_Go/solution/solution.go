package solution

import (
	"fmt"
	"strings"
	"time"
)

func countHillValley(nums []int) int {
	// 0ms
	i, res, dirrection := 0, 0, true
	for i < len(nums)-1 {
		if nums[i] == nums[i+1] {
			i++
			continue
		}
		dirrection = (nums[i] < nums[i+1])
		i++
		break
	}
	for i < len(nums)-1 {
		if dirrection {
			if nums[i] > nums[i+1] {
				dirrection = false
				res++
			}
		} else {
			if nums[i] < nums[i+1] {
				dirrection = true
				res++
			}
		}
		i++
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := countHillValley(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

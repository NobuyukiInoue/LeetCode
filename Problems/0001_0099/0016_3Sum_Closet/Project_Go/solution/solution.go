package solution

import (
	"fmt"
	"math"
	"sort"
	"strconv"
	"strings"
	"time"
)

func threeSumClosest(nums []int, target int) int {
	// 13ms
	min, result := math.MaxInt, 0
	sort.Sort(sort.IntSlice(nums))
	for i := 0; i < len(nums)-2; i++ {
		j, k := i+1, len(nums)-1
		for j < k {
			sum := nums[i] + nums[j] + nums[k]
			diff := myAbs(sum - target)
			if diff == 0 {
				return sum
			}
			if diff < min {
				min = diff
				result = sum
			}
			if sum <= target {
				j++
			} else {
				k--
			}
		}
	}
	return result
}

func myAbs(a int) int {
	if a > 0 {
		return a
	}
	return -a
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

	result := threeSumClosest(nums, target)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

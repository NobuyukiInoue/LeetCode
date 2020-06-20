package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func searchRange(nums []int, target int) []int {
	low, high := math.MaxInt32, 0
	hit := false
	for _, cur := range nums {
		if cur == target {
			hit = true
		}
	}
	if !hit {
		return []int{-1, -1}
	}

	for i := 0; i < len(nums); i++ {
		if nums[i] == target {
			if i > high {
				high = i
			}
			if i < low {
				low = i
			}
		}
	}
	return []int{low, high}
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

	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))
	fmt.Printf("target = %d\n", target)

	timeStart := time.Now()

	result := searchRange(nums, target)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

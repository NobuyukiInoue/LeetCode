package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func makesquare(nums []int) bool {
	// 0ms
	numsSum := 0

	for _, num := range nums {
		numsSum += num
	}

	if numsSum == 0 || numsSum%4 != 0 {
		return false
	}

	sort.Sort(sort.Reverse(sort.IntSlice(nums)))

	side := numsSum / 4
	sides := []int{0, 0, 0, 0}

	return dfs(sides, 0, nums, side)
}

func dfs(sides []int, index int, nums []int, side int) bool {
	if index == len(nums) {
		return true
	}

	curr := nums[index]
	for i := 0; i < 4; i++ {
		if i > 0 && sides[i] == sides[i-1] {
			continue
		}
		if sides[i]+curr <= side {
			sides[i] += curr
			if dfs(sides, index+1, nums, side) {
				return true
			}
			sides[i] -= curr
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := makesquare(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

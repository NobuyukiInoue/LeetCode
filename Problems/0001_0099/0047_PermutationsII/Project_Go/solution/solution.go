package solution

import (
	"fmt"
	"strings"
	"time"
)

func permuteUnique(nums []int) [][]int {
	// 8ms
	ans := [][]int{}
	helper(&ans, 0, nums)
	return ans
}

func helper(ans *[][]int, depth int, nums []int) {
	if depth == len(nums) {
		*ans = append(*ans, append([]int{}, nums...))
	}

	used := make(map[int]int)
	for i := depth; i < len(nums); i++ {
		if _, ok := used[nums[i]]; ok {
			continue
		}

		nums[i], nums[depth] = nums[depth], nums[i]
		helper(ans, depth+1, nums)
		nums[i], nums[depth] = nums[depth], nums[i]

		used[nums[i]] = i
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	nums := StringToIntArray(flds)

	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))
	timeStart := time.Now()

	result := permuteUnique(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

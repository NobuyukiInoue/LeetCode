package solution

import (
	"fmt"
	"strconv"
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

func strToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intintArrayToString(nums [][]int) string {
	if len(nums) <= 0 {
		return ""
	}
	resultStr := "[" + intArrayToString(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + intArrayToString(nums[i])
	}

	return resultStr + "]"
}

func intArrayToString(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := "[" + strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	nums := strToIntArray(flds)

	fmt.Printf("nums = %s\n", intArrayToString(nums))
	timeStart := time.Now()

	result := permuteUnique(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", intintArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

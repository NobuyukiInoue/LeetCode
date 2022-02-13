package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findFinalValue(nums []int, original int) int {
	// 4ms
	for contains(nums, original) {
		original *= 2
	}
	return original
}

func contains(nums []int, target int) bool {
	for _, v := range nums {
		if target == v {
			return true
		}
	}
	return false
}

func findFinalValue_with_array1000(nums []int, original int) int {
	// 4ms
	var store [1001]int
	for i := 0; i < len(nums); i++ {
		store[nums[i]]++
	}
	ans := original
	for store[ans] >= 1 {
		store[ans] = 0
		ans *= 2
		if ans > 1000 {
			break
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	nums := StringToIntArray(flds[0])
	original, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = [%s], original = %d\n", IntArrayToString(nums), original)

	timeStart := time.Now()

	result := findFinalValue(nums, original)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

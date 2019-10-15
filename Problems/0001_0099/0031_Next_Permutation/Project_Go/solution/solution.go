package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func nextPermutation(nums []int) {
	p := len(nums) - 1
	for ; p > 0 && nums[p] <= nums[p-1]; p-- {
	}

	if p == 0 {
		reverse(nums, 0, len(nums)-1)
		return
	}

	q := len(nums) - 1
	for ; nums[q] <= nums[p-1]; q-- {
	}

	temp := nums[p-1]
	nums[p-1] = nums[q]
	nums[q] = temp
	reverse(nums, p, len(nums)-1)
}

func reverse(a []int, from int, to int) {
	for ; from < to; from++ {
		temp := a[from]
		a[from] = a[to]
		a[to] = temp
		to--
	}
}

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func printIntArray(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := str2IntArray(flds)
	fmt.Printf("nums = %s\n", printIntArray(nums))

	timeStart := time.Now()

	nextPermutation(nums)

	timeEnd := time.Now()

	fmt.Printf("nums = %s\n", printIntArray(nums))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

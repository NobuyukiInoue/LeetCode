package solution

import (
	"fmt"
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

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	nextPermutation(nums)

	timeEnd := time.Now()

	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func maxFrequency(nums []int, k int) int {
	// 245ms
	res, left, right := 1, 0, 0
	sum := 0
	sort.Sort(sort.IntSlice(nums))
	for right = 0; right < len(nums); right++ {
		sum += nums[right]
		for sum+k < nums[right]*(right-left+1) {
			sum -= nums[left]
			left++
		}
		res = myMax(res, right-left+1)
	}
	return res
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = %s, k = %d\n", IntArrayToString(nums), k)

	timeStart := time.Now()

	result := maxFrequency(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

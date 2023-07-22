package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func partitionArray(nums []int, k int) int {
	// 194ms - 215ms
	sort.Sort(sort.IntSlice(nums))
	ans, start := 1, nums[0]
	for i := 1; i < len(nums); i++ {
		diff := nums[i] - start
		if diff > k {
			ans++
			start = nums[i]
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = [%s], k = %d\n", IntArrayToString(nums), k)

	timeStart := time.Now()

	result := partitionArray(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

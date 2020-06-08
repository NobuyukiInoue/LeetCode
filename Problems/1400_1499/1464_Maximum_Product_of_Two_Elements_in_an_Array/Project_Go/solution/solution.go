package solution

import (
	"fmt"
	"math"
	"sort"
	"strconv"
	"strings"
	"time"
)

func maxProduct(nums []int) int {
	// 4ms
	m := math.MinInt64
	n := m
	for _, num := range nums {
		if num >= m {
			n = m
			m = num
		} else if num > n {
			n = num
		}
	}
	return (m - 1) * (n - 1)
}

func maxProduct2(nums []int) int {
	// 4ms
	sort.Sort(sort.IntSlice(nums))
	lenNums := len(nums)
	return ((nums[lenNums-1] - 1) * (nums[lenNums-2] - 1))
}

func strToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intArrayToString(nums []int) string {
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

	nums := strToIntArray(flds)
	fmt.Printf("nums = [%s]\n", intArrayToString(nums))

	timeStart := time.Now()

	result := maxProduct(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

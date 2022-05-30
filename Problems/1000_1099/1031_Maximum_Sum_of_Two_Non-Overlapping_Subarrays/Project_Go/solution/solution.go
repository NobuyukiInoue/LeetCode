package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func maxSumTwoNoOverlap(nums []int, firstLen int, secondLen int) int {
	// 0ms - 6ms
	for i := 1; i < len(nums); i++ {
		nums[i] += nums[i-1]
	}
	f, s := firstLen, secondLen
	maxf, maxs, maxt := nums[f-1], nums[s-1], nums[f+s-1]
	for i := f + s; i < len(nums); i++ {
		maxf = myMax(maxf, nums[i-s]-nums[i-s-f])
		maxs = myMax(maxs, nums[i-f]-nums[i-f-s])
		maxt = myMax(maxt, myMax(maxf+nums[i]-nums[i-s], maxs+nums[i]-nums[i-f]))
	}
	return maxt
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
	firstLen, _ := strconv.Atoi(flds[1])
	secondLen, _ := strconv.Atoi(flds[2])
	fmt.Printf("nums = [%s], firstLen = %d, secondLen = %d\n", IntArrayToString(nums), firstLen, secondLen)

	timeStart := time.Now()

	result := maxSumTwoNoOverlap(nums, firstLen, secondLen)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

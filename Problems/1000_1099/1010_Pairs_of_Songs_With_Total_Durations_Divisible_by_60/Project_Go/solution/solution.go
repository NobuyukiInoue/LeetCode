package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func numPairsDivisibleBy60(time []int) int {
	freq := make([]int, 60)
	for _, dur := range time {
		freq[dur%60]++
	}

	res := 0
	for i := 1; i < 30; i++ {
		res += freq[i] * freq[60-i]
	}

	res += freq[0] * (freq[0] - 1) / 2
	res += freq[30] * (freq[30] - 1) / 2

	return res
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

	vartime := str2IntArray(flds)
	fmt.Printf("time = %s\n", printIntArray(vartime))

	timeStart := time.Now()

	result := numPairsDivisibleBy60(vartime)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

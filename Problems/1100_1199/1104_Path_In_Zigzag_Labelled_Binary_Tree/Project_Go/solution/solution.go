package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func pathInZigZagTree(label int) []int {
	level, s := 1, 1
	for ; s < label; level++ {
		s += 1 << uint(level)
	}
	res := make([]int, level)
	res[0], res[level-1] = 1, label
	for level -= 2; level > 0; level-- {
		s >>= 1
		label = s - (label-s+1)/2 + 1
		res[level] = label
	}
	return res
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
	fld := strings.Replace(temp, "]", "", -1)

	label, _ := strconv.Atoi(fld)
	fmt.Printf("label = %d\n", label)

	timeStart := time.Now()

	result := pathInZigZagTree(label)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", printIntArray(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

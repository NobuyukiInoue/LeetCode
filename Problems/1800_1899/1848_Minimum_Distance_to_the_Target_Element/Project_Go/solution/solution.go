package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func getMinDistance(nums []int, target int, start int) int {
	// 0ms
	ans := math.MaxInt64
	for i, n := range nums {
		if n == target {
			ans = myMin(ans, myAbs(i-start))
		}
	}
	return ans
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func myAbs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	fmt.Printf("nums = %s\n", IntArrayToString(nums))
	flds2 := StringToIntArray(flds[1])
	target := flds2[0]
	start := flds2[1]
	fmt.Printf("target = %d, start = %d\n", target, start)

	timeStart := time.Now()

	result := getMinDistance(nums, target, start)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

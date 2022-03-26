package solution

import (
	"fmt"
	"strings"
	"time"
)

func minOperations(nums []int) int {
	// 32ms - 48ms
	cntAdd, cntDbl, tmp := 0, 0, 0
	for _, num := range nums {
		if num != 0 {
			cntAdd++
		}
		tmp = 0
		for num > 1 {
			cntAdd += num & 1
			tmp++
			num >>= 1
		}
		cntDbl = myMax(tmp, cntDbl)
	}
	return cntDbl + cntAdd
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := minOperations(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

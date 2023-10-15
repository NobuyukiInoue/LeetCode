package solution

import (
	"fmt"
	"strings"
	"time"
)

func maximumTripletValue(nums []int) int64 {
	// 0ms
	res, maxa, maxab := int64(0), int64(0), int64(0)
	for _, num := range nums {
		l_num := int64(num)
		res = myMax(res, maxab*l_num)
		maxab = myMax(maxab, maxa-l_num)
		maxa = myMax(maxa, l_num)
	}
	return res
}

func myMax(a, b int64) int64 {
	if a >= b {
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

	result := maximumTripletValue(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

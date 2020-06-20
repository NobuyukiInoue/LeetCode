package solution

import (
	"fmt"
	"strings"
	"time"
)

func singleNumber(nums []int) int {
	// 4ms
	ones, twos := 0, 0
	for _, v := range nums {
		ones = (ones ^ v) & ^twos
		twos = (twos ^ v) & ^ones
	}
	return ones
}

func singleNumber2(nums []int) int {
	// 4ms
	mymap := make(map[int]int)

	for _, target := range nums {
		var val int
		v, ok := mymap[target]
		if ok {
			val = v + 1
		} else {
			val = 1
		}
		mymap[target] = val
	}

	for k, v := range mymap {
		if v == 1 {
			return k
		}
	}

	return 0
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := singleNumber(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func arithmeticTriplets(nums []int, diff int) int {
	// 5ms - 9ms
	occ := make(map[int]int, 0)
	for _, num := range nums {
		occ[num] = 1
	}
	ans := 0
	for _, num := range nums {
		if _, ok := occ[num+diff]; ok {
			if _, ok := occ[2*(num+diff)-num]; ok {
				ans++
			}
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	nums := StringToIntArray(flds[0])
	diff, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = [%s], diff = %d\n", IntArrayToString(nums), diff)

	timeStart := time.Now()

	result := arithmeticTriplets(nums, diff)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

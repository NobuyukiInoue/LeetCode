package solution

import (
	"fmt"
	"strings"
	"time"
)

func lengthOfLIS(nums []int) int {
	tails := make([]int, len(nums))
	size := 0
	for _, x := range nums {
		i, j := 0, size
		for i != j {
			m := (i + j) / 2
			if tails[m] < x {
				i = m + 1
			} else {
				j = m
			}
		}
		tails[i] = x
		if i == size {
			size++
		}
	}
	return size
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := lengthOfLIS(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

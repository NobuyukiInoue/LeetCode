package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isPossibleToSplit(nums []int) bool {
	// 0ms
	var cnts [100]int
	for _, num := range nums {
		cnts[num-1]++
		if cnts[num-1] == 3 {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := isPossibleToSplit(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

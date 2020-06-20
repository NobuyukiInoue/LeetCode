package solution

import (
	"fmt"
	"strings"
	"time"
)

func decompressRLElist(nums []int) []int {
	// 76ms
	res := make([]int, 0)
	for i := 0; i < len(nums); i += 2 {
		repeats, numToRepeat := nums[i], nums[i+1]

		for j := 0; j < repeats; j++ {
			res = append(res, numToRepeat)
		}
	}

	return res
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

	result := decompressRLElist(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

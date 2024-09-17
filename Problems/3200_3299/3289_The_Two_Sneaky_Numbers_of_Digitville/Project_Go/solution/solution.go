package solution

import (
	"fmt"
	"strings"
	"time"
)

func getSneakyNumbers(nums []int) []int {
	// 3ms
	cnts := make(map[int]int, 0)
	var ans []int
	for _, num := range nums {
		cnts[num]++
		if cnts[num] == 2 {
			ans = append(ans, num)
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := getSneakyNumbers(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

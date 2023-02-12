package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func separateDigits(nums []int) []int {
	// 0ms
	var ans []int
	for _, num := range nums {
		s_num := strconv.Itoa(num)
		for _, ch := range s_num {
			ans = append(ans, int(ch-'0'))
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

	result := separateDigits(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

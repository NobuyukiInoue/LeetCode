package solution

import (
	"fmt"
	"strings"
	"time"
)

func resultArray(nums []int) []int {
	// 0ms
	var arr1, arr2 []int
	last1, last2 := nums[0], nums[1]
	arr1, arr2 = append(arr1, last1), append(arr2, last2)
	for _, num := range nums[2:] {
		if last1 > last2 {
			arr1 = append(arr1, num)
			last1 = num
		} else {
			arr2 = append(arr2, num)
			last2 = num
		}
	}
	return append(arr1, arr2...)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := resultArray(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

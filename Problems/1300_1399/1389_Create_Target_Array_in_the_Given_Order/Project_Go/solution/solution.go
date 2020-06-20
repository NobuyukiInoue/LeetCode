package solution

import (
	"fmt"
	"strings"
	"time"
)

func createTargetArray(nums []int, index []int) []int {
	// 0ms
	targetArray := make([]int, len(nums))
	for i, idx := range index {
		copy(targetArray[idx+1:i+1], targetArray[idx:i])
		targetArray[idx] = nums[i]
	}
	return targetArray
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	index := StringToIntArray(flds[1])
	fmt.Printf("nums  = [%s]\n", IntArrayToString(nums))
	fmt.Printf("index = [%s]\n", IntArrayToString(index))

	timeStart := time.Now()

	result := createTargetArray(nums, index)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

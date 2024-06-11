package solution

import (
	"fmt"
	"strings"
	"time"
)

func continuousSubarrays(nums []int) int64 {
	// 103ms - 128ms
	countMap := make(map[int]int, 0)
	j := 0
	count := int64(0)
	for i, num := range nums {
		countMap[num] = 1 + countMap[num]
		for i-j+1 > getCount(num, countMap) {
			countMap[nums[j]] = countMap[nums[j]] - 1
			j++
		}
		count += int64(i) - int64(j) + int64(1)
	}
	return count
}

func getCount(num int, countMap map[int]int) int {
	return countMap[num] + countMap[num-1] + countMap[num+1] + countMap[num-2] + countMap[num+2]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := continuousSubarrays(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

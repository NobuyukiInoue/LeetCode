package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func circularArrayLoop(nums []int) bool {
	// 1ms
	n := len(nums)
	visited := make([]bool, n)
	for i := 0; i < n; i++ {
		if visited[i] {
			continue
		}
		dic := make(map[int]bool, 0)
		forward := (nums[i] >= 0)
		index := i
		for {
			visited[index] = true
			newIndex := (index + nums[index]) % n
			if newIndex < 0 {
				newIndex += n
			}
			if index == newIndex || forward != (nums[newIndex] >= 0) {
				break
			}

			if _, ok := dic[index]; ok {
				return true
			}
			dic[index] = true
			index = newIndex
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := circularArrayLoop(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func mostFrequent(nums []int, key int) int {
	// 7ms
	cnts := map[int]int{}
	target, max_cnts := 0, 0
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] == key {
			cnts[nums[i+1]] += 1
			if max_cnts < cnts[nums[i+1]] {
				target, max_cnts = nums[i+1], cnts[nums[i+1]]
			}
		}
	}
	return target
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	nums := StringToIntArray(flds[0])
	key, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = [%s], key = %d\n", IntArrayToString(nums), key)

	timeStart := time.Now()

	result := mostFrequent(nums, key)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

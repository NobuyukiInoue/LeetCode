package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findKDistantIndices(nums []int, key int, k int) []int {
	// 0ms - 6ms
	var indices []int
	i, len_nums := 0, len(nums)
	for j, _ := range nums {
		if nums[j] == key {
			if len(indices) == 0 {
				i = 0
			} else {
				i = indices[len(indices)-1] + 1
			}
			i = myMax(j-k, i)
			end := myMin(j+k, len_nums-1)
			for ; i <= end; i++ {
				indices = append(indices, i)
			}
		}
	}
	return indices
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
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
	k, _ := strconv.Atoi(flds[2])
	fmt.Printf("nums = [%s], key = %d, k = %d\n", IntArrayToString(nums), key, k)

	timeStart := time.Now()

	result := findKDistantIndices(nums, key, k)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func countPairs(nums []int, k int) int {
	// 4ms
	ans, len_nums := 0, len(nums)
	for i := 0; i < len_nums-1; i++ {
		for j := i + 1; j < len_nums; j++ {
			if nums[i] != nums[j] {
				continue
			}
			if i*j%k == 0 {
				ans++
			}
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = [%s], k = %d\n", IntArrayToString(nums), k)

	timeStart := time.Now()

	result := countPairs(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

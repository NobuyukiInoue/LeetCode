package solution

import (
	"fmt"
	"strings"
	"time"
)

func distinctDifferenceArray(nums []int) []int {
	// 16ms - 20ms
	ans := make([]int, len(nums))
	pref := make(map[int]int, 0)
	suff := make(map[int]int, 0)
	for _, num := range nums {
		pref[num]++
	}
	for i, num := range nums {
		suff[num]++
		pref[num]--
		if pref[num] == 0 {
			delete(pref, num)
		}
		ans[i] = len(suff) - len(pref)
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

	result := distinctDifferenceArray(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

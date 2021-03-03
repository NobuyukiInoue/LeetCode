package solution

import (
	"fmt"
	"strings"
	"time"
)

func findMaxLength(nums []int) int {
	// 104ms
	dic := map[int]int{}
	dic[0] = -1
	total, ans := 0, 0
	for i, num := range(nums) {
		if num == 0 {
			total--
		} else {
			total++
		}
		if index, exist := dic[total]; exist {
			ans = myMax(i - index, ans)
		} else {
			dic[total] = i
		}
	}
	return ans
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := findMaxLength(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

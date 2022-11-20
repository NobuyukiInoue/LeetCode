package solution

import (
	"fmt"
	"strings"
	"time"
)

func countNicePairs(nums []int) int {
	// 98ms - 126ms
	dic := make(map[int]int, 0)
	res := 0
	for _, num := range nums {
		temp := num - reverse(num)
		if val, ok := dic[temp]; ok {
			res += val
		}
		res %= 1000000007
		dic[temp]++
	}
	res = res % 1000000007
	return res
}

func reverse(num int) int {
	ans := 0
	for num != 0 {
		ans = ans*10 + num%10
		num /= 10
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

	result := countNicePairs(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxSum(nums []int) int {
	// 12ms - 15ms
	dic := make(map[int]int, 0)
	res := -1
	for _, num := range nums {
		max_digit := getMaxDigit(num)
		if val, ok := dic[max_digit]; ok {
			res = myMax(res, num+val)
		}
		dic[max_digit] = myMax(num, dic[max_digit])
	}
	return res
}

func getMaxDigit(num int) int {
	maxDigit := 0
	for num > 0 {
		maxDigit = myMax(maxDigit, num%10)
		num /= 10
	}
	return maxDigit
}

func myMax(a, b int) int {
	if a >= b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := maxSum(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

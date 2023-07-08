package solution

import (
	"fmt"
	"strings"
	"time"
)

func countBeautifulPairs(nums []int) int {
	// 48ms - 52ms
	ans := 0
	for i, num := range nums {
		m := num % 10
		for j := 0; j < i; j++ {
			n := nums[j]
			for n >= 10 {
				n /= 10
			}
			if gcd(m, n) == 1 {
				ans++
			}
		}
	}
	return ans
}

func gcd(m, n int) int {
	for n > 0 {
		m, n = n, m%n
	}
	return m
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := countBeautifulPairs(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

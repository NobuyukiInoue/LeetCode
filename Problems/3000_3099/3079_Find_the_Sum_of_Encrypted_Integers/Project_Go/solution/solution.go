package solution

import (
	"fmt"
	"strings"
	"time"
)

func sumOfEncryptedInt(nums []int) int {
	// 0ms
	ans := 0
	for _, num := range nums {
		m, l := 0, 0
		for num > 0 {
			m = myMax(m, num%10)
			num /= 10
			l++
		}
		for ; l > 0; l-- {
			ans += m
			m *= 10
		}
	}
	return ans
}

func myMax(a, b int) int {
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
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := sumOfEncryptedInt(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

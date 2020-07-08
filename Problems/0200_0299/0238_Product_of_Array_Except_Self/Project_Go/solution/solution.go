package solution

import (
	"fmt"
	"strings"
	"time"
)

func productExceptSelf(nums []int) []int {
	// 16ms
	numsLength := len(nums)
	res := make([]int, numsLength)
	postfix := make([]int, numsLength)

	res[0] = 1
	postfix[numsLength - 1] = 1

	for i := 1; i < numsLength; i++ {
		res[i] = res[i - 1]*nums[i - 1]
	}

	for i := numsLength - 2; i >= 0; i-- {
		postfix[i] = postfix[i + 1]*nums[i + 1]
	}

	for i := 0; i < numsLength; i++ {
		res[i] = res[i]*postfix[i]
	}

	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := productExceptSelf(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

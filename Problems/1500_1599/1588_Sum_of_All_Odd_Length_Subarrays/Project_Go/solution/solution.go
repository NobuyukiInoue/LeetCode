package solution

import (
	"fmt"
	"strings"
	"time"
)

func sumOddLengthSubarrays(arr []int) int {
	// 0ms
	sum := 0
	for i := 1; i <= len(arr); i += 2 {
		sum += slidingSum(arr, i)
	}
	return sum
}

func slidingSum(arr []int, windowSize int) int {
	res, sum := 0, 0
	for i := 0; i < len(arr); i++ {
		if i < windowSize {
			sum += arr[i]
		} else {
			res += sum
			sum -= arr[i-windowSize]
			sum += arr[i]
		}
	}
	return res + sum
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	arr := StringToIntArray(flds)
	fmt.Printf("arr = [%s]\n", IntArrayToString(arr))

	timeStart := time.Now()

	result := sumOddLengthSubarrays(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

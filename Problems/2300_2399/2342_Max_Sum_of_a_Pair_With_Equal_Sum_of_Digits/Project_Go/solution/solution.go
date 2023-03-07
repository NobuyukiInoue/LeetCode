package solution

import (
	"fmt"
	"strings"
	"time"
)

func maximumSum(nums []int) int {
	// 108ms - 116ms
	digitSumToNum := [81]int32{}
	result := int32(-1)
	for i := 0; i < len(nums); i++ {
		num := int32(nums[i])
		var digitsSum byte
		for num := num; num != 0; num /= 10 {
			digitsSum += byte(num % 10)
		}
		num2 := digitSumToNum[digitsSum-1]
		if num2 != 0 {
			sum := num + num2
			if sum > result {
				result = sum
			}
		}
		if num > num2 {
			digitSumToNum[digitsSum-1] = num
		}
	}
	return int(result)
}

func maximumSum_use_map(nums []int) int {
	// 132ms - 135ms
	dict_map := make(map[int]int, 0)
	max_val := -1
	for i, num := range nums {
		digits_sum := 0
		for num > 0 {
			digits_sum += num % 10
			num /= 10
		}
		if _, ok := dict_map[digits_sum]; ok {
			new_max_val := nums[i] + dict_map[digits_sum]
			max_val = myMax(max_val, new_max_val)
			dict_map[digits_sum] = myMax(nums[i], dict_map[digits_sum])
		} else {
			dict_map[digits_sum] = nums[i]
		}
	}
	return max_val
}

func Contains(nums []int, target int) bool {
	for _, num := range nums {
		if num == target {
			return true
		}
	}
	return false
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

	result := maximumSum(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

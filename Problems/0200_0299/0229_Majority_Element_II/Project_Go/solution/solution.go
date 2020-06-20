package solution

import (
	"fmt"
	"strings"
	"time"
)

func majorityElement(nums []int) []int {
	// 12ms
	numsLength := len(nums)

	var res []int
	limit := numsLength / 3
	mymap := make(map[int]int)

	for _, target := range nums {
		var val int
		v, ok := mymap[target]
		if ok {
			val = v + 1
		} else {
			val = 1
		}
		mymap[target] = val

		if val > limit {
			if contains(res, target) == false {
				res = append(res, target)
			}
		}
	}
	return res
}

func contains(s []int, e int) bool {
	for _, v := range s {
		if e == v {
			return true
		}
	}
	return false
}

func majorityElement2(nums []int) []int {
	// 12ms
	if nums == nil || len(nums) == 0 {
		return []int{}
	}

	var result []int
	number1, number2 := nums[0], nums[0]
	count1, count2 := 0, 0
	numsLen := len(nums)
	for i := 0; i < numsLen; i++ {
		if nums[i] == number1 {
			count1++
		} else if nums[i] == number2 {
			count2++
		} else if count1 == 0 {
			number1 = nums[i]
			count1 = 1
		} else if count2 == 0 {
			number2 = nums[i]
			count2 = 1
		} else {
			count1--
			count2--
		}
	}
	count1, count2 = 0, 0
	for i := 0; i < numsLen; i++ {
		if nums[i] == number1 {
			count1++
		} else if nums[i] == number2 {
			count2++
		}
	}
	if count1 > numsLen/3 {
		result = append(result, number1)
	}
	if count2 > numsLen/3 {
		result = append(result, number2)
	}
	return result
}

func strArrayToString(data []string) string {
	if len(data) <= 0 {
		return ""
	}

	resultStr := data[0]
	for i := 1; i < len(data); i++ {
		resultStr += ", " + data[i]
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := majorityElement(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

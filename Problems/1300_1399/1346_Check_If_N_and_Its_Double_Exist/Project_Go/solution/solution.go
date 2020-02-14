package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func checkIfExist2(arr []int) bool {
	// 4ms
	lst := make(map[int]bool, 0)
	for _, num := range arr {
		if num%2 == 0 {
			if _, ok := lst[num/2]; ok {
				return true
			}
		}
		if _, ok := lst[num*2]; ok {
			return true
		}
		lst[num] = true
	}
	return false
}

func checkIfExist(arr []int) bool {
	// 4ms
	lst := make([]int, 0)
	for _, num := range arr {
		if contains(lst, num*2) || num%2 == 0 && contains(lst, num/2) {
			return true
		}
		lst = append(lst, num)
	}
	return false
}

func contains(lst []int, num int) bool {
	for _, v := range lst {
		if v == num {
			return true
		}
	}
	return false
}

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intintArrayToString(nums [][]int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := "[" + intArrayToString(nums[0]) + "]"
	for i := 1; i < len(nums); i++ {
		resultStr += ", [" + intArrayToString(nums[i]) + "]"
	}

	return resultStr
}

func intArrayToString(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	arr := str2IntArray(flds)
	fmt.Printf("arr = [%s]\n", intArrayToString(arr))

	timeStart := time.Now()

	result := checkIfExist(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
